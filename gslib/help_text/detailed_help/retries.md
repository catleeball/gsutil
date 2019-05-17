# RETRY STRATEGY
  There are a number of reasons that gsutil operations can fail; some are not
  retryable, and require that the user take some action, for example:

  - Invalid credentials
  - Network unreachable because of a proxy configuration problem
  - Access denied, because the bucket or object you are trying to use has an
    ACL that doesn't permit the action you're trying to perform.

  In other cases errors are retryable - transient network failures and HTTP 429
  and 5xx error codes. For these cases, gsutil will retry using a truncated
  binary exponential backoff strategy:

  - Wait a random period between [0..1] seconds and retry;
  - If that fails, wait a random period between [0..2] seconds and retry;
  - If that fails, wait a random period between [0..4] seconds and retry;
  - And so on, up to a configurable maximum number of retries (default = 23),
  with each retry period bounded by a configurable maximum period of time
  (default = 60 seconds).

  Thus, by default, gsutil will retry 23 times over 1+2+4+8+16+32+60... seconds
  for about 10 minutes. You can adjust the number of retries and maximum delay
  of any individual retry by editing the num_retries and max_retry_delay
  configuration variables in the "[Boto]" section of the .boto config file.
  Most users shouldn't need to change these values.

  For data transfers (the gsutil cp and rsync commands), gsutil provides
  additional retry functionality, in the form of resumable transfers.
  Essentially, a transfer that was interrupted because of a transient error
  can be restarted without starting over from scratch. For more details
  about this, see the "RESUMABLE TRANSFERS" section of "gsutil help cp".