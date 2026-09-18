# Privilege Escalation

## Description
Privilege escalation is an attempt to obtain permissions higher than those currently available to a user or process.

## Detection Indicators
- Failed privilege escalation attempts
- Unexpected administrative commands
- Attempts to access restricted resources
- Suspicious changes to permissions or privileged accounts

## Investigation
- Identify the user involved.
- Identify the source host or IP.
- Review commands and authentication events.
- Check for successful privilege escalation afterward.
- Review changes to privileged accounts and permissions.

## Defensive Response
- Investigate the affected account and host.
- Restrict unnecessary administrative privileges.
- Review authentication and authorization controls.
- Monitor the system for additional suspicious activity.

## Important
A failed privilege escalation attempt does not prove that privilege escalation was successful.