import pandas as pd

# Load the CSV files
df_spain = pd.read_csv("Artefact/Data/percentageRenewableElectricityFiltered-Esp.csv")
df_ireland = pd.read_csv("Artefact/Data/percentageRenewableElectricityFiltered-Irl.csv")

# Get the most recent available values
last_year_spain = df_spain["Year"].iloc[-1]
last_mean_spain = df_spain["Mean"].iloc[-1]

last_year_ireland = df_ireland["Year"].iloc[-1]
last_mean_ireland = df_ireland["Mean"].iloc[-1]

# Calculate the average growth over the past 4 years (2023-2020)
growth_spain = (df_spain["Mean"].iloc[-1] - df_spain["Mean"].iloc[-4]) / 4
growth_ireland = (df_ireland["Mean"].iloc[-1] - df_ireland["Mean"].iloc[-4]) / 4

# Generate recommendations based on the data
recommendations = f"""
<h3>Comparison Between Spain and Ireland in {last_year_spain}</h3>
<p>In {last_year_spain}, the percentage of renewable electricity in Spain was <strong>{last_mean_spain:.2f}%</strong>, 
while in Ireland it was <strong>{last_mean_ireland:.2f}%</strong>.</p>

<h3>Long-Term Trends</h3>
<p>Over the past 4 years, Spain has had an average annual growth of <strong>{growth_spain:.2f}%</strong> in renewable energy, 
while Ireland has grown at a rate of <strong>{growth_ireland:.2f}%</strong> per year.</p>

<h3>Recommendations Based on These Findings</h3>
<ul>
    <li>Spain’s renewable energy growth rate (<strong>{growth_spain:.2f}%</strong>) is significantly higher than Ireland’s (<strong>{growth_ireland:.2f}%</strong>), with a difference of <strong>{(growth_spain - growth_ireland):.2f}%</strong> per year. This suggests that Spain’s policies and investments are yielding stronger results, while Ireland may need to accelerate its transition effrots.</li>

    <li>Spain should continue investing in wind and solar energy to sustain its higher-than-average 
        growth rate of <strong>{growth_spain:.2f}%</strong> per year.</li>
    
    <li>Ireland needs to accelerate its transition, as its growth rate of <strong>{growth_ireland:.2f}%</strong> per year 
        is significantly lower than Spain's.</li>

    <li>Grid modernization is crucial for both countries: Spain should invest in smart grids to manage 
        its increasing renewable share, while Ireland should expand its storage capacity to stabilize supply.</li>

    <li>Policy alignment with EU targets: Spain is on track but should ensure long-term sustainability, 
        while Ireland must introduce stronger incentives to increase its renewable share more rapidly.</li>

    <li>Public and private sector collaboration: Spain can attract further investments due to its high growth, 
        while Ireland needs policies that encourage faster adoption of renewables.</li>
</ul>
"""

#save file
output_folder = "Report/Presentation"
output_path = f"{output_folder}/recommendations.html"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(recommendations)

print(f"The file {output_path} has been generated.")