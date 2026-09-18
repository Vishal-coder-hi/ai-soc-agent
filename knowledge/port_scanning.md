# Port Scanning

## Description
Port scanning is a reconnaissance technique used to discover network services and exposed ports on a host.

## Detection Indicators
- Multiple ports accessed from the same source
- Sequential connection attempts to different ports
- Scanning of common services such as SSH, HTTP and HTTPS

## Investigation
- Identify the source IP.
- Identify the destination host.
- Determine which ports were targeted.
- Check whether the source is internal or external.
- Review subsequent activity from the same source.

## Defensive Response
- Investigate the scanned host.
- Restrict unnecessary exposed services.
- Apply firewall rules where appropriate.
- Monitor the source for additional suspicious activity.

## Important
Port scanning indicates reconnaissance activity but does not prove that exploitation occurred.