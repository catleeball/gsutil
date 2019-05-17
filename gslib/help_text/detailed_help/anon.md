# OVERVIEW
  gsutil users can access publicly readable data without obtaining
  credentials. For example, the gs://uspto-pair bucket contains a number
  of publicly readable objects, so any user can run the following command
  without first obtaining credentials:

    gsutil ls gs://uspto-pair/applications/0800401*

  Users can similarly download objects they find via the above gsutil ls
  command.

  See "gsutil help acls" for more details about data protection.

# Configuring/Using Credentials via Cloud SDK Distribution of gsutil
  If a user without credentials attempts to access protected data using gsutil,
  they will be prompted to run gcloud init to obtain credentials.

# Configuring/Using Credentials via Standalone gsutil Distribution
  If a user without credentials attempts to access protected data using gsutil,
  they will be prompted to run gsutil config to obtain credentials.