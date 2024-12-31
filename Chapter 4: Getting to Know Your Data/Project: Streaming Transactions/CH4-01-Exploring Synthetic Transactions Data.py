# Databricks notebook source
# MAGIC %md
# MAGIC Chapter 4: Getting to Know Your Data
# MAGIC
# MAGIC ## Streaming data - Exploration
# MAGIC Currently you cannot access streaming tables from a single user cluster. Shared ML runtime + UC is also not avilable. For this notebook we use non DLT streaming table for exploration so we don't need to create another cluster. However, if you do want to explore `synthetic_transactions_dlt`, you can use a shared cluster with a standard DBR 13+.

# COMMAND ----------

# MAGIC %md ## Run Setup

# COMMAND ----------

# MAGIC %run ../../global-setup $project_name=synthetic_transactions

# COMMAND ----------

# MAGIC %md
# MAGIC ## Visualize the streaming table

# COMMAND ----------

# DBTITLE 1,Simple select allows many visualizations
# MAGIC %sql
# MAGIC select * from synthetic_transactions

# COMMAND ----------

import seaborn as sns

# Check the schema of the DataFrame
df = spark.table('synthetic_transactions').toPandas()
print(df.columns)

# Adjust the column names if necessary
g = sns.PairGrid(df[['CustomerID', 'Amount',  'Label']], diag_sharey=False, hue="Label")
g.map_lower(sns.kdeplot).map_diag(sns.kdeplot, lw=3).map_upper(sns.regplot).add_legend()
