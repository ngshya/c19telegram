from pandas import read_csv
import matplotlib.pylab as plt

df_data = read_csv(
    filepath_or_buffer="https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv", 
    parse_dates=["data"]
)
df_data.sort_values(["data"], inplace=True)

df_data["nuovi_tamponi"] = df_data["tamponi"].diff()
df_data["positivi_su_tamponi"] = df_data["nuovi_positivi"] / df_data["nuovi_tamponi"]
df_data["nuovi_deceduti"] = df_data["deceduti"].diff()

fig, ax = plt.subplots(figsize=(14, 7))
df_data.loc[:, ["positivi_su_tamponi", "nuovi_positivi"]].plot(secondary_y='nuovi_positivi', ax=ax, color=["darkblue", "darkred"])
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.title("ANDAMENTO NAZIONALE " + str(df_data["data"].max()))
plt.tight_layout()
plt.savefig('andamento_nazionale_1.png')

fig, ax = plt.subplots(figsize=(14, 7))
df_data.loc[:, ["totale_ospedalizzati", "nuovi_deceduti"]].plot(secondary_y='nuovi_deceduti', ax=ax, color=["darkorange", "black"])
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.title("ANDAMENTO NAZIONALE " + str(df_data["data"].max()))
plt.tight_layout()
plt.savefig('andamento_nazionale_2.png')

df_data = read_csv(
    filepath_or_buffer="https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv", 
    usecols = ["data", "sigla_provincia", "totale_casi"]
)
df_data = df_data.loc[df_data.sigla_provincia == "TO", :]
df_data.sort_values(["data"], inplace=True)
df_data["nuovi_positivi"] = df_data["totale_casi"].diff()

fig, ax = plt.subplots(figsize=(14, 7))
df_data.loc[:, ["nuovi_positivi"]].plot(ax=ax)
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.title("ANDAMENTO PROVINCIA DI TORINO " + str(df_data["data"].max()))
plt.tight_layout()
plt.savefig('andamento_torino.png')
