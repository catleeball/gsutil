# SYNOPSIS
  gsutil help [command or topic]


# DESCRIPTION
  Running:

    gsutil help

  will provide a summary of all commands and additional topics on which
  help is available.

  Running:

    gsutil help command or topic

  will provide help about the specified command or topic.

  Running:

    gsutil help command sub-command

  will provide help about the specified sub-command. For example, running:

    gsutil help acl set

  will provide help about the "set" subcommand of the "acl" command.

  If you set the PAGER environment variable to the path to a pager program
  (such as /bin/less on Linux), long help sections will be piped through
  the specified pager.
