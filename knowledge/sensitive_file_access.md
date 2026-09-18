# Sensitive File Access

## Description
Access to sensitive system files can provide information about users, configuration or system security.

## Detection Indicators
- Unexpected access to sensitive files
- Access by unusual users or processes
- Repeated access to system configuration files

## Investigation
- Identify the user or process accessing the file.
- Determine whether the access was expected.
- Review surrounding authentication and process activity.
- Check whether additional sensitive files were accessed.

## Defensive Response
- Validate whether the access was authorized.
- Monitor related activity.
- Apply appropriate file and system access controls.
- Investigate suspicious processes or accounts.

## Important
Accessing a sensitive file is not automatically malicious. Context, user identity and process behavior must be considered.