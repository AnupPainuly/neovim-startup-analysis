import pandas as pd
from matplotlib import pyplot as plt

dat = pd.read_csv("profile.csv", header=None, names=["TraceTime", "SourceTime", "ExecTime", "PluginName"])
dat_n = dat.groupby("PluginName")["ExecTime"].sum().reset_index()
dat_n_sorted = dat_n.sort_values("ExecTime", ascending=False)
top_10 = dat_n_sorted.head(10)
#print(top_10.to_string(index = False))
dat_n_sorted.to_csv("results.csv",index = False)


# Create a bar chart with custom styling
plt.figure(figsize=(10, 6))
plt.bar(top_10["PluginName"], top_10["ExecTime"], color="skyblue")
plt.xlabel("Plugin Name", fontsize=12)
plt.ylabel("Exec Time", fontsize=12)
plt.title("Top 10 Plugins by Exec Time", fontsize=14)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Display the bar chart
plt.savefig("bar_char.png")

# Prepare data for the pie chart
top_5 = dat_n_sorted.head(5)
sizes = top_5["ExecTime"]
labels=top_5["PluginName"]
colors = ["#2E5B88", "#497AA7", "#73A4CA", "#9FCAE6", "#B9DDF1"]
explode = [0.1] + [0] * (len(sizes) - 1)  # Explode the first slice for emphasis

# Plot bar chart
fig = plt.figure(4, figsize = (8,8))
ax = fig.add_subplot(211)
pie = ax.pie(sizes,startangle = 0, explode=explode, shadow = True, autopct = '%1.1f%%',colors = colors)
ax2 = fig.add_subplot(212)
ax2.axis("off")
ax2.legend(pie[0], labels,  loc="upper left")
plt.tight_layout()
plt.savefig("pie_chart.png")
