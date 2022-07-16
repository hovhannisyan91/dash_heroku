import plotly.express as px

long_df = px.data.medals_long()

fig_1 = px.bar(long_df, x="nation", y="count", color="medal", title="Sample Bar Plot")

# --------------------------------- #
wide_df = px.data.medals_wide()

fig_2 = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")										