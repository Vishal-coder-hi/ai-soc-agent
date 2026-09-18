# Brute Force Attack

## Description
A brute force attack attempts to gain access to an account by repeatedly trying passwords or authentication credentials.

## Detection Indicators
- Multiple failed login attempts
- Repeated authentication failures from the same IP
- Successful login after many failed attempts
- Login attempts targeting privileged accounts

## Investigation
- Identify the source IP address.
- Count failed authentication attempts.
- Check whether a successful login occurred afterward.
- Identify the targeted account.
- Review authentication logs around the same time.
- Check whether the source IP is known or suspicious.

## Defensive Response
- Temporarily block or rate-limit the suspicious source.
- Enable account lockout or authentication throttling where appropriate.
- Enforce strong passwords and MFA.
- Investigate successful authentication following repeated failures.

## Important
A high number of failed login attempts is suspicious, but it does not by itself prove that an account was compromised.