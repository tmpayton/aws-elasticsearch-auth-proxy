# AWS ES Authentication Proxy

This is a reverse-proxy used to expose AWS Elasticsearch instances without authentication.

It's inherently insecure and should be used only for testing with non-production, non-sensitive, non-essential data.

## usage

1. Update cf/sample-secrets.yml
2. Log into CF, targeting the org and space that have your elasticsearch service instance
3. run `./dev cf` to push the app
4. Open an ssh tunnel with `cf ssh -L 8080:localhost:8080 auth-proxy`
5. Use localhost:8080 to access your elasticsearch cluster as you normally would
