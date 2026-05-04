from shiny import App, render, ui, reactive
import pandas as pd
import io

# 1. The UI (What you see)
app_ui = ui.page_fluid(
    ui.h2("HTS Dose-Response Calculator"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_numeric("stock_conc", "Stock Concentration (mM):", 10.0),
            ui.input_numeric("dilution_factor", "Serial Dilution (1:X):", 3.0),
            ui.input_numeric("points", "Number of Points:", 7),
            ui.input_numeric("transfer_vol", "Transfer Volume (nL):", 20.0),
            ui.input_numeric("assay_vol", "Assay Volume (µL):", 5.0),
            ui.br(),
            # Discreet credit in gray
            ui.div(
                "Made by Colin Gordy", 
                style="color: gray; font-size: 0.8em; font-style: italic; margin-top: 20px;"
            )
        ),
        ui.h4("Final Well Concentrations"),
        ui.output_data_frame("dose_table"),
        ui.br(),
        ui.download_button("download_excel", "Export to Excel"),
        ui.br(),
        ui.br(),
        ui.output_text_verbatim("summary")
    )
)

# 2. The Server (The Math)
def server(input, output, session):
    
    @reactive.calc
    def generate_dose_data():
        stock = input.stock_conc()
        dil_factor = input.dilution_factor()
        pts = int(input.points())
        t_vol = input.transfer_vol()
        a_vol_nl = input.assay_vol() * 1000 # Convert µL to nL

        dilution_ratio = (t_vol + a_vol_nl) / t_vol
        
        data = []
        current_stock = stock

        for i in range(1, pts + 1):
            final_conc = current_stock / dilution_ratio
            data.append({
                "Point": i,
                "Stock Plate (mM)": round(current_stock, 4),
                "Final Well (µM)": round(final_conc * 1000, 4)
            })
            current_stock = current_stock / dil_factor 

        return pd.DataFrame(data)

    @render.data_frame
    def dose_table():
        return generate_dose_data()
    
    @render.download(filename="dose_response_setup.xlsx")
    def download_excel():
        df = generate_dose_data()
        
        with io.BytesIO() as buffer:
            df.to_excel(buffer, index=False)
            yield buffer.getvalue()
    
    @render.text
    def summary():
        t_vol = input.transfer_vol()
        a_vol_nl = input.assay_vol() * 1000
        ratio = (t_vol + a_vol_nl) / t_vol
        return f"Physical Transfer Dilution Ratio: 1 to {round(ratio)}"

# 3. Combine them
app = App(app_ui, server)