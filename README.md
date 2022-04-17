# Requirements:

- [ ]  Create a Terraform module that is a RDS Instance where subnets are passed.
- [ ]  Create a Django Task that runs daily that copies a postgresql database from the primary database host to a secondary database host.
    - [ ]  The copied database should be of the form canal_prod_<mm>_<dd>_<yyyy>
- [ ]  Write the cron task for this deployment.