import pandas as pd #for CSV access
import plotly.express as px #for basic graphs
import plotly.graph_objects as go #for comparing graphhs

#Read CSV files and store in separate variables
df = pd.read_csv("./Artefact/Data/percentageRenewableElectricityFiltered-Esp.csv")
df1 = pd.read_csv("./Artefact/Data/percentageRenewableElectricityFiltered-Irl.csv")
df_2023 = df[df["Year"] == 2023]
df1_2023 = df1[df1["Year"] == 2023]

#Calculating the non renewable percentage for 2023 which is not directly stated in the CSV (100 - renewable)
esp_renewable_2023 = df_2023["Mean"].values[0]
esp_non_renewable_2023 = 100 - esp_renewable_2023
irl_renewable_2023 = df1_2023["Mean"].values[0]
irl_non_renewable_2023 = 100 - irl_renewable_2023

#Create a def so i dont have to rewrite the funcion each time to style the graphs
#Removing control buttons as i thought they do not look good and all actions can be performed using the mouse and keyboard anyway
def customize_plot(fig):
    fig.update_layout(
        showlegend=False,
        modebar=dict(
            remove=["autoScale2d", "autoscale",
                    "editInChartStudio", "editinchartstudio",
                    "hoverCompareCartesian", "hovercompare",
                    "lasso", "lasso2d", "orbitRotation",
                    "orbitrotation", "pan", "pan2d", "pan3d",
                    "reset", "resetCameraDefault3d",
                    "resetCameraLastSave3d", "resetGeo",
                    "resetSankeyGroup", "resetScale2d",
                    "resetViewMap", "resetViewMapbox",
                    "resetViews", "resetcameradefault",
                    "resetcameralastsave", "resetsankeygroup",
                    "resetscale", "resetview", "resetviews",
                    "select", "select2d", "sendDataToCloud",
                    "senddatatocloud", "tableRotation",
                    "tablerotation", "toImage", "toggleHover",
                    "toggleSpikelines", "togglehover",
                    "togglespikelines", "toimage", "zoom",
                    "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo",
                    "zoomInMap", "zoomInMapbox", "zoomOut2d",
                    "zoomOutGeo", "zoomOutMap", "zoomOutMapbox",
                    "zoomin", "zoomout"]
        ),
    )
    return fig

#A def to make numbers on axis always whole as i think it is not ideal to put years as decimals
def full_num_axis(fig):
    fig.update_xaxes(
     tickmode="linear",
        dtick=1
    )
    return fig

#Create line grahps of each set of data
fig = px.line(df, x="Year", y="Mean")
fig = customize_plot(fig)
fig = full_num_axis(fig)

fig1 = px.line(df1, x="Year", y="Mean")
fig1 = customize_plot(fig1)
fig1 = full_num_axis(fig1)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df["Year"], y=df["Mean"], mode="lines", name="Spain"))
fig2.add_trace(go.Scatter(x=df1["Year"], y=df1["Mean"], mode="lines", name="Ireland"))
fig2 = customize_plot(fig2)
fig2 = full_num_axis(fig2)

fig3 = px.bar(
    x=["Spain Renewable", "Spain Non renewable", "Ireland Renewable", "Ireland Non Renewable"],
    y=[esp_renewable_2023, esp_non_renewable_2023, irl_renewable_2023, irl_non_renewable_2023],
    title="Renewable Energy only in 2023 Spain vs Ireland",
        color=["Spain Renewable", "Spain Non renewable", "Ireland Renewable", "Ireland Non Renewable"],
    color_discrete_map={
        "Spain Renewable": "red",
        "Spain Non renewable": "orange",
        "Ireland Renewable": "green",
        "Ireland Non Renewable": "navy"
    }
)
fig3 = customize_plot(fig3)


fig3.update_layout(
    xaxis_title="Category",
    yaxis_title="Percentage",
    showlegend=False
)

fig3.show()

fig.write_html("Artefact/Graphs/graphRenewableEnergy-Esp.html")
fig1.write_html("Artefact/Graphs/graphRenewableEnergy-Irl.html")
fig2.write_html("Artefact/Graphs/graphRenewableEnergy-Compare.html")
fig3.write_html("Artefact/Graphs/graphRenewableEnergyVsNonRenewable.html")
