import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from plotly.offline import iplot
import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)



st.title("World Population  🌎")
st.markdown("Analysis of Population 🌎")



df=pd.read_csv('C:\WORKSPACE\world_popolution_age.csv')


st.sidebar.title("Select Country 🌎 ")
select=st.sidebar.selectbox('Please Choose',['Afghanistan', 'Africa', 'African Group', 'African Union',
       'African Union: Central Africa', 'African Union: Eastern Africa',
       'African Union: Northern Africa', 'African Union: Southern Africa',
       'African Union: Western Africa',
       'African, Caribbean and Pacific (ACP) Group of States', 'Albania',
       'Algeria', 'Andean Community', 'Angola', 'Antigua and Barbuda',
       'Argentina', 'Armenia', 'Aruba', 'Asia',
       'Asia-Pacific Economic Cooperation (APEC)', 'Asia-Pacific Group',
       'Association of Southeast Asian Nations (ASEAN)', 'Australia',
       'Australia/New Zealand', 'Austria', 'Azerbaijan', 'BRIC', 'BRICS',
       'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
       'Belgium', 'Belize', 'Belt-Road Initiative (BRI)',
       'Belt-Road Initiative: Africa', 'Belt-Road Initiative: Asia',
       'Belt-Road Initiative: Europe',
       'Belt-Road Initiative: Latin America and the Caribbean',
       'Belt-Road Initiative: Pacific', 'Benin', 'Bhutan',
       'Black Sea Economic Cooperation (BSEC)',
       'Bolivarian Alliance for the Americas (ALBA)',
       'Bolivia (Plurinational State of)', 'Bosnia and Herzegovina',
       'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria',
       'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon',
       'Canada', 'Caribbean',
       'Caribbean Community and Common Market (CARICOM)',
       'Central African Republic', 'Central America', 'Central Asia',
       'Central European Free Trade Agreement (CEFTA)',
       'Central and Southern Asia', 'Chad', 'Channel Islands', 'Chile',
       'China', 'China (and dependencies)', 'China, Hong Kong SAR',
       'China, Macao SAR', 'China, Taiwan Province of China', 'Colombia',
       'Commonwealth of Independent States (CIS)',
       'Commonwealth of Nations', 'Commonwealth: Africa',
       'Commonwealth: Asia', 'Commonwealth: Caribbean and Americas',
       'Commonwealth: Europe', 'Commonwealth: Pacific', 'Comoros',
       'Congo', 'Costa Rica', 'Countries with Access to the Sea',
       'Countries with Access to the Sea: Africa',
       'Countries with Access to the Sea: Asia',
       'Countries with Access to the Sea: Europe',
       'Countries with Access to the Sea: Latin America and the Caribbean',
       'Countries with Access to the Sea: Northern America',
       'Countries with Access to the Sea: Oceania', 'Croatia', 'Cuba',
       'Curaçao', 'Cyprus', 'Czechia', "Côte d'Ivoire",
       "Dem. People's Republic of Korea",
       'Democratic Republic of the Congo', 'Denmark',
       'Denmark (and dependencies)', 'Djibouti', 'Dominican Republic',
       'ECE: North America-2', 'ECE: UNECE-52', 'ECLAC: Latin America',
       'ECLAC: The Caribbean', 'ESCAP region: East and North-East Asia',
       'ESCAP region: North and Central Asia', 'ESCAP region: Pacific',
       'ESCAP region: South and South-West Asia',
       'ESCAP region: South-East Asia',
       'ESCAP: ADB Developing member countries (DMCs)',
       'ESCAP: ADB Group A (Concessional assistance\xa0only)',
       'ESCAP: ADB Group B\xa0(OCR blend)',
       'ESCAP: ADB Group C (Regular OCR only)', 'ESCAP: ASEAN',
       'ESCAP: Central Asia', 'ESCAP: ECO', 'ESCAP: HDI groups',
       'ESCAP: Landlocked countries (LLDCs)',
       'ESCAP: Least Developed Countries (LDCs)',
       'ESCAP: Pacific island dev. econ.', 'ESCAP: SAARC',
       'ESCAP: WB High income econ.', 'ESCAP: WB Low income econ.',
       'ESCAP: WB Lower middle income econ.',
       'ESCAP: WB Upper middle income econ.', 'ESCAP: WB income groups',
       'ESCAP: high HDI', 'ESCAP: high income', 'ESCAP: income groups',
       'ESCAP: low HDI', 'ESCAP: low income', 'ESCAP: lower middle HDI',
       'ESCAP: lower middle income',
       'ESCAP: other Asia-Pacific countries/areas',
       'ESCAP: upper middle HDI', 'ESCAP: upper middle income',
       'ESCWA: Arab countries', 'ESCWA: Arab least developed countries',
       'ESCWA: Gulf Cooperation Council countries',
       'ESCWA: Maghreb countries', 'ESCWA: Mashreq countries',
       'ESCWA: member countries', 'East African Community (EAC)',
       'Eastern Africa', 'Eastern Asia', 'Eastern Europe',
       'Eastern European Group', 'Eastern and South-Eastern Asia',
       'Economic Community of Central African States (ECCAS)',
       'Economic Community of West African States (ECOWAS)',
       'Economic Cooperation Organization (ECO)', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Eswatini', 'Ethiopia', 'Eurasian Economic Community (Eurasec)',
       'Europe', 'Europe (48)', 'Europe and Northern America',
       'European Community (EC: 12)',
       'European Free Trade Agreement (EFTA)', 'European Union (EU: 15)',
       'European Union (EU: 28)', 'Fiji', 'Finland', 'France',
       'France (and dependencies)', 'French Guiana', 'French Polynesia',
       'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
       'Greater Arab Free Trade Area (GAFTA)', 'Greece', 'Grenada',
       'Group of 77 (G77)', 'Group of Eight (G8)', 'Group of Seven (G7)',
       'Group of Twenty (G20) - member states', 'Guadeloupe', 'Guam',
       'Guatemala', 'Guinea', 'Guinea-Bissau',
       'Gulf Cooperation Council (GCC)', 'Guyana', 'Haiti',
       'High-income countries', 'Honduras', 'Hungary', 'Iceland', 'India',
       'Indonesia', 'Iran (Islamic Republic of)', 'Iraq', 'Ireland',
       'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
       'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'LLDC: Africa',
       'LLDC: Asia', 'LLDC: Europe', 'LLDC: Latin America',
       'Land-locked Countries', 'Land-locked Countries (Others)',
       'Land-locked Developing Countries (LLDC)',
       "Lao People's Democratic Republic",
       'Latin America and the Caribbean',
       'Latin American Integration Association (ALADI)',
       'Latin American and Caribbean Group (GRULAC)', 'Latvia',
       'League of Arab States (LAS, informal name: Arab League)',
       'Least developed countries', 'Least developed: Africa',
       'Least developed: Asia',
       'Least developed: Latin America and the Caribbean',
       'Least developed: Oceania', 'Lebanon', 'Lesotho',
       'Less developed regions',
       'Less developed regions, excluding China',
       'Less developed regions, excluding least developed countries',
       'Less developed: Africa', 'Less developed: Asia',
       'Less developed: Latin America and the Caribbean',
       'Less developed: Oceania', 'Liberia', 'Libya', 'Lithuania',
       'Low-income countries', 'Lower-middle-income countries',
       'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
       'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius',
       'Mayotte', 'Melanesia', 'Mexico', 'Micronesia',
       'Micronesia (Fed. States of)', 'Middle Africa',
       'Middle-income countries', 'Mongolia', 'Montenegro',
       'More developed regions', 'More developed: Asia',
       'More developed: Europe', 'More developed: Northern America',
       'More developed: Oceania', 'Morocco', 'Mozambique', 'Myanmar',
       'Namibia', 'Nepal', 'Netherlands',
       'Netherlands (and dependencies)', 'New Caledonia',
       'New EU member states (joined since 2004)', 'New Zealand',
       'New Zealand (and dependencies)', 'Nicaragua', 'Niger', 'Nigeria',
       'No income group available', 'Non-Self-Governing Territories',
       'North American Free Trade Agreement (NAFTA)',
       'North Atlantic Treaty Organization (NATO)', 'North Macedonia',
       'Northern Africa', 'Northern Africa and Western Asia',
       'Northern America', 'Northern Europe', 'Norway', 'Oceania',
       'Oceania (excluding Australia and New Zealand)', 'Oman',
       'Organisation for Economic Co-operation and Development (OECD)',
       'Organization for Security and Co-operation in Europe (OSCE)',
       'Organization of American States (OAS)',
       'Organization of Petroleum Exporting countries (OPEC)',
       'Organization of the Islamic Conference (OIC)', 'Pakistan',
       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
       'Poland', 'Polynesia', 'Portugal', 'Puerto Rico', 'Qatar',
       'Republic of Korea', 'Republic of Moldova', 'Romania',
       'Russian Federation', 'Rwanda', 'Réunion',
       'SIDS Atlantic, and Indian Ocean, Mediterranean and South China Sea (AIMS)',
       'SIDS Caribbean', 'SIDS Pacific', 'Saint Lucia',
       'Saint Vincent and the Grenadines', 'Samoa',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Shanghai Cooperation Organization (SCO)',
       'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
       'Small Island Developing States (SIDS)', 'Solomon Islands',
       'Somalia', 'South Africa', 'South America',
       'South Asian Association for Regional Cooperation (SAARC)',
       'South Sudan', 'South-Eastern Asia', 'Southern Africa',
       'Southern African Development Community (SADC)', 'Southern Asia',
       'Southern Common Market (MERCOSUR)', 'Southern Europe', 'Spain',
       'Sri Lanka', 'State of Palestine', 'Sub-Saharan Africa', 'Sudan',
       'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
       'Tajikistan', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga',
       'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
       'UN-ECE: member countries', 'UNFPA Regions',
       'UNFPA: Arab States (AS)', 'UNFPA: Asia and the Pacific (AP)',
       'UNFPA: East and Southern Africa (ESA)',
       'UNFPA: Eastern Europe and Central Asia (EECA)',
       'UNFPA: Latin America and the Caribbean (LAC)',
       'UNFPA: West and Central Africa (WCA)', 'UNICEF PROGRAMME REGIONS',
       'UNICEF Programme Regions: East Asia and Pacific (EAPRO)',
       'UNICEF Programme Regions: Eastern Caribbean',
       'UNICEF Programme Regions: Eastern and Southern Africa (ESARO)',
       'UNICEF Programme Regions: Europe and Central Asia (CEECIS)',
       'UNICEF Programme Regions: Latin America',
       'UNICEF Programme Regions: Latin America and Caribbean (LACRO)',
       'UNICEF Programme Regions: Middle East and North Africa (MENARO)',
       'UNICEF Programme Regions: South Asia (ROSA)',
       'UNICEF Programme Regions: West and Central Africa (WCARO)',
       'UNICEF REGIONS', 'UNICEF Regions: East Asia and Pacific',
       'UNICEF Regions: Eastern Europe and Central Asia',
       'UNICEF Regions: Eastern and Southern Africa',
       'UNICEF Regions: Europe and Central Asia',
       'UNICEF Regions: Latin America and Caribbean',
       'UNICEF Regions: Middle East and North Africa',
       'UNICEF Regions: North America', 'UNICEF Regions: South Asia',
       'UNICEF Regions: Sub-Saharan Africa',
       'UNICEF Regions: West and Central Africa',
       'UNICEF Regions: Western Europe',
       'UNITED NATIONS Regional Groups of Member States', 'Uganda',
       'Ukraine', 'United Arab Emirates', 'United Kingdom',
       'United Kingdom (and dependencies)',
       'United Nations Economic Commission for Africa (UN-ECA)',
       'United Nations Economic Commission for Latin America and the Caribbean (UN-ECLAC)',
       'United Nations Economic and Social Commission for Asia and the Pacific (UN-ESCAP) Regions',
       'United Nations Member States', 'United Republic of Tanzania',
       'United States Virgin Islands', 'United States of America',
       'United States of America (and dependencies)',
       'Upper-middle-income countries', 'Uruguay', 'Uzbekistan',
       'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam',
       'WB region: East Asia and Pacific (excluding high income)',
       'WB region: Europe and Central Asia (excluding high income)',
       'WB region: Latin America and Caribbean (excluding high income)',
       'WB region: Middle East and North Africa (excluding high income)',
       'WB region: South Asia (excluding high income)',
       'WB region: Sub-Saharan Africa (excluding high income)',
       'WHO Regions', 'WHO: African region (AFRO)',
       'WHO: Americas (AMRO)', 'WHO: Eastern Mediterranean Region (EMRO)',
       'WHO: European Region (EURO)',
       'WHO: South-East Asia region (SEARO)',
       'WHO: Western Pacific region (WPRO)',
       'West African Economic and Monetary Union (UEMOA)',
       'Western Africa', 'Western Asia', 'Western Europe',
       'Western European and Others Group (WEOG)', 'Western Sahara',
       'World', 'World Bank Regional Groups (developing only)', 'Yemen',
       'Zambia', 'Zimbabwe'],key='1')



st.title(select)
choice=st.sidebar.selectbox('Choose the Preferred Visualization',['Histogram','Scatter','Heatmap'])

if not st.sidebar.checkbox("Do not Show", True):

    if choice =='Histogram':
        fig=px.histogram(df[df['Location']==select],x='AgeGrp',y='PopTotal')
        st.plotly_chart(fig)


    elif choice =='Scatter':
        fig=px.scatter(df[df['Location']==select],x='AgeGrp',y='PopTotal')
        st.plotly_chart(fig)
     
    else:

        fig=px.density_heatmap(df[df['Location']==select],x='AgeGrp',y='PopTotal')
        st.plotly_chart(fig)


st.sidebar.title("Choose the Gender")
sc=st.sidebar.selectbox("Please choose",['Male','Female'])


if not st.sidebar.checkbox("Hide",True):

    if sc=="Male" and choice == 'Histogram':
        fig=px.histogram(df[df['Location']==select],x='AgeGrp',y='PopMale')
        st.plotly_chart(fig)

    elif sc=="Male" and choice == 'Scatter':
        fig=px.scatter(df[df['Location']==select],x='AgeGrp',y='PopMale')
        st.plotly_chart(fig)

    elif sc=="Male" and choice == 'Heatmap':
        fig=px.density_heatmap(df[df['Location']==select],x='AgeGrp',y='PopMale')
        st.plotly_chart(fig)

    elif sc=="Female" and choice == 'Scatter':
        fig=px.scatter(df[df['Location']==select],x='AgeGrp',y='PopFemale')
        st.plotly_chart(fig)

    elif sc=="Female" and choice == 'Heatmap':
        fig=px.density_heatmap(df[df['Location']==select],x='AgeGrp',y='PopFemale')
        st.plotly_chart(fig)

    else:
        fig=px.histogram(df[df['Location']==select],x='AgeGrp',y='PopFemale')
        st.plotly_chart(fig)




if st.sidebar.checkbox('Show Whole Dataset',False):
    st.write(df)

    
    
















    











































