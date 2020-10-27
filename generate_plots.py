from pandas import read_csv
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
from numpy import unique, array


pp = PdfPages('COVID-19-ITALIA.pdf')


df_data = read_csv(
    filepath_or_buffer="https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv", 
    parse_dates=["data"]
)
df_data.sort_values(["data"], inplace=True)
df_data.reset_index(drop=True, inplace=True)

array_xticks = array([_ for _ in range(len(df_data.index))])
array_bool_xticks = (array_xticks % 7) == 0
array_xticks = array_xticks[array_bool_xticks]
array_xlabels = df_data.data[array_bool_xticks]
array_xlabels = [str(x).split(" ")[0] for x in array_xlabels]

df_data["nuovi_tamponi"] = df_data["tamponi"].diff()
df_data["positivi_su_tamponi"] = df_data["nuovi_positivi"] / df_data["nuovi_tamponi"]
df_data["nuovi_deceduti"] = df_data["deceduti"].diff()
df_data["nuovi_casi_testati"] = df_data["casi_testati"].diff()
df_data["positivi_su_casi_testati"] = df_data["nuovi_positivi"] / df_data["nuovi_casi_testati"]

fig, ax = plt.subplots(figsize=(14, 7))
df_data.loc[:, ["positivi_su_tamponi", "nuovi_positivi"]].plot(secondary_y='nuovi_positivi', ax=ax, color=["darkblue", "darkred"], rot="vertical")
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.title("ANDAMENTO NAZIONALE " + str(df_data["data"].max()))
plt.xticks(ticks=array_xticks, labels=array_xlabels)
plt.tight_layout()
plt.savefig(pp, format='pdf')

fig, ax = plt.subplots(figsize=(14, 7))
df_data.loc[:, ["positivi_su_casi_testati", "nuovi_positivi"]].plot(secondary_y='nuovi_positivi', ax=ax, color=["darkcyan", "darkred"], rot="vertical")
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.title("ANDAMENTO NAZIONALE " + str(df_data["data"].max()))
plt.xticks(ticks=array_xticks, labels=array_xlabels)
plt.tight_layout()
plt.savefig(pp, format='pdf')

fig, ax = plt.subplots(figsize=(14, 7))
df_data.loc[:, ["totale_ospedalizzati", "nuovi_deceduti"]].plot(secondary_y='nuovi_deceduti', ax=ax, color=["darkorange", "black"], rot="vertical")
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.title("ANDAMENTO NAZIONALE " + str(df_data["data"].max()))
plt.xticks(ticks=array_xticks, labels=array_xlabels)
plt.tight_layout()
plt.savefig(pp, format='pdf')

df_data = read_csv(
    filepath_or_buffer="https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv", 
    parse_dates=["data"],
    usecols=["data", "denominazione_regione", "totale_ospedalizzati", "nuovi_positivi", "deceduti", "tamponi"]
)
df_data.sort_values(["data"], inplace=True)
array_regioni = sorted(unique(df_data.denominazione_regione))

for r in array_regioni:

    df_data_r = df_data.copy(deep=True).loc[df_data.denominazione_regione == r, :]
    df_data_r.reset_index(drop=True, inplace=True)

    df_data_r["nuovi_tamponi"] = df_data_r["tamponi"].diff()
    df_data_r["positivi_su_tamponi"] = df_data_r["nuovi_positivi"] / df_data_r["nuovi_tamponi"]
    df_data_r.loc[df_data_r.positivi_su_tamponi < 0, ["positivi_su_tamponi"]] = 0
    df_data_r["nuovi_deceduti"] = df_data_r["deceduti"].diff()

    fig, ax = plt.subplots(figsize=(14, 7))
    df_data_r.loc[:, ["positivi_su_tamponi", "nuovi_positivi"]].plot(secondary_y='nuovi_positivi', ax=ax, color=["darkblue",  "darkred"], rot="vertical")
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title("Andamento " + r + " " + str(df_data_r["data"].max()))
    plt.xticks(ticks=array_xticks, labels=array_xlabels)
    plt.tight_layout()
    plt.savefig(pp, format='pdf')

    fig, ax = plt.subplots(figsize=(14, 7))
    df_data_r.loc[:, ["totale_ospedalizzati", "nuovi_deceduti"]].plot(secondary_y='nuovi_deceduti', ax=ax, color= ["darkorange", "black"], rot="vertical")
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    plt.title("Andamento " + r + " " + str(df_data_r["data"].max()))
    plt.xticks(ticks=array_xticks, labels=array_xlabels)
    plt.tight_layout()
    plt.savefig(pp, format='pdf')

pp.close()