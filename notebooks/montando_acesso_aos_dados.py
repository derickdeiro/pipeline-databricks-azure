# Databricks notebook source
# MAGIC %scala
# MAGIC dbutils.fs.mkdirs("/mnt/dados")

# COMMAND ----------

dbutils.fs.ls("/mnt")

# COMMAND ----------

# MAGIC %scala
# MAGIC val configs = Map(
# MAGIC   "fs.azure.account.auth.type" -> "OAuth",
# MAGIC   "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC   "fs.azure.account.oauth2.client.id" -> "145922d4-3ac1-4cf2-82e5-609e526eeb62",
# MAGIC   "fs.azure.account.oauth2.client.secret" -> "Rfc8Q~ZAO23K8Exdd7gjQ1GfeE1iEkErXj6Z2c7X",
# MAGIC   "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com/893deab8-867b-4b2d-a0ce-fc934bca5fe1/oauth2/token")
# MAGIC // Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC dbutils.fs.mount(
# MAGIC   source = "abfss://imoveis@datalakedeiro.dfs.core.windows.net/",
# MAGIC   mountPoint = "/mnt/dados",
# MAGIC   extraConfigs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/dados")

# COMMAND ----------


