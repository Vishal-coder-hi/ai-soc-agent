# 🛡️ AI SOC Agent

An AI-powered Security Operations Center (SOC) platform that detects suspicious security activity, enriches alerts with threat intelligence, performs risk assessment, retrieves security knowledge using RAG, generates AI-assisted analysis and response plans, correlates alerts into incidents, and presents results through a web dashboard.

---

## 📌 Project Overview

Traditional SOC environments generate a large number of security alerts that require continuous monitoring and manual investigation.

This project demonstrates an AI-assisted SOC workflow that automates several stages of the security monitoring process.

The platform combines:

- Security log analysis
- Threat detection
- Threat intelligence
- Risk scoring
- Retrieval-Augmented Generation (RAG)
- AI security analysis
- Incident investigation
- AI-generated response planning
- Multi-agent orchestration
- Incident storage
- Security dashboard
- Centralized logging

The system is designed as a **production-style educational SOC platform prototype**.

---

## 🎯 Problem Statement

Security analysts often need to:

1. Monitor security logs
2. Identify suspicious activity
3. Investigate alerts
4. Check threat intelligence
5. Determine risk
6. Correlate multiple alerts
7. Prepare incident response actions

Performing these tasks manually can be time-consuming.

The goal of this project is to demonstrate how AI and automation can assist SOC analysts by creating a structured security-analysis pipeline.

---

## 💡 Solution

The AI SOC Agent processes security events through multiple stages.

```text
Security Logs
     │
     ▼
Detection Agent
     │
     ▼
Threat Intelligence
     │
     ▼
Risk Scoring
     │
     ▼
Security RAG
     │
     ▼
AI SOC Analyst
     │
     ▼
Investigation Agent
     │
     ▼
Response Agent
     │
     ▼
Incident Storage
     │
     ▼
SOC Dashboard
```

---

🚀 Key Features
1. Security Log Detection

The system analyzes security logs and identifies suspicious activities such as:

Multiple failed login attempts
Port scanning
Sensitive file access
Failed privilege escalation

Example:

Login failed user=admin ip=185.220.101.5

Multiple failed attempts from the same IP can trigger a brute-force alert.

2. Threat Intelligence

External threat intelligence can be used to enrich IP-based alerts.

The project integrates with:

VirusTotal API

The system can retrieve information such as:

Reputation
Malicious detections
Suspicious detections
Country
Autonomous System / organization information

Private IP addresses are detected locally and public threat-intelligence lookup is skipped for them.

3. Risk Scoring

The platform calculates a numerical risk score between:

0 - 100

Risk levels include:

LOW
MEDIUM
HIGH
CRITICAL

Risk scoring considers factors such as:

Alert severity
Threat intelligence results
Failed login attempts

Example:

Possible Brute Force Attack
Risk Score: 86
Risk Level: CRITICAL
4. Security RAG

The platform includes a local security knowledge base.

Knowledge files include:

knowledge/
├── brute_force.md
├── port_scanning.md
├── privilege_escalation.md
└── sensitive_file_access.md

The RAG engine retrieves relevant security knowledge based on the detected alert.

This information is then supplied to the AI analyst as reference material.

The system explicitly distinguishes:

Observed Security Evidence
        ≠
Retrieved Security Knowledge

This helps reduce unsupported conclusions.

5. AI SOC Analyst

The AI analyst analyzes enriched security alerts using an OpenAI-compatible Qwen API.

The analyst produces:

Attack Type
Severity
Risk Assessment
Why the Activity Is Suspicious
Possible Attacker Objective
Investigation Steps
Recommended Defensive Action

The AI is instructed not to claim that an attack succeeded unless the available evidence supports it.

6. Investigation Agent

The Investigation Agent correlates multiple alerts and generates an incident investigation.

It evaluates possible relationships between events such as:

Network Reconnaissance
        ↓
Credential Attack
        ↓
Sensitive File Access
        ↓
Privilege Escalation Attempt

The system treats these relationships as possible correlations rather than automatically assuming that all events belong to the same attacker.

7. Response Agent

The Response Agent generates a structured response plan containing:

1. Immediate Actions
2. Investigation Actions
3. Containment Actions
4. Recovery Actions
5. Monitoring Actions
6. Analyst Decision

The system is designed around analyst-assisted response rather than automatically executing destructive security actions.

🤖 Multi-Agent Architecture

The project contains multiple logical security agents.

                 ┌──────────────────────┐
                 │     Security Logs    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Detection Agent    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Threat Intel Agent   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Risk Scoring      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Security RAG     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    AI SOC Analyst    │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
   ┌────────────────────┐      ┌────────────────────┐
   │ Investigation Agent│      │   Response Agent   │
   └──────────┬─────────┘      └──────────┬─────────┘
              │                           │
              └─────────────┬─────────────┘
                            ▼
                 ┌──────────────────────┐
                 │   Incident Storage   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    SOC Dashboard     │
                 └──────────────────────┘
🧠 Technology Stack
Technology	Purpose
Python	Core application
Flask	SOC Dashboard
Qwen	AI security analysis
OpenAI Python SDK	AI API integration
VirusTotal API	Threat Intelligence
RAG	Security knowledge retrieval
JSON	Local incident storage
Python Logging	Centralized application logging
HTML/CSS	Dashboard interface
Git/GitHub	Version control
📂 Project Structure
ai-soc-agent/
│
├── agents/
│   ├── detection_agent.py
│   ├── investigation_agent.py
│   ├── orchestrator.py
│   ├── response_agent.py
│   └── threat_intel_agent.py
│
├── analyzer/
│   ├── ai_analyst.py
│   ├── investigation_agent.py
│   ├── log_parser.py
│   ├── rag_engine.py
│   ├── response_agent.py
│   ├── risk_scorer.py
│   ├── storage.py
│   └── threat_intel.py
│
├── config/
│
├── core/
│   ├── logger.py
│   └── soc_pipeline.py
│
├── dashboard/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── knowledge/
│   ├── brute_force.md
│   ├── port_scanning.md
│   ├── privilege_escalation.md
│   └── sensitive_file_access.md
│
├── logs/
│   └── security.log
│
├── services/
│   └── incident_store.py
│
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
⚙️ Installation
1. Clone the repository
git clone https://github.com/Vishal-coder-hi/ai-soc-agent.git
cd ai-soc-agent
2. Create virtual environment
python3 -m venv venv

Activate it:

macOS / Linux
source venv/bin/activate
Windows
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
🔐 Configuration

Create a .env file:

QWEN_API_KEY=your_qwen_api_key
VT_API_KEY=your_virustotal_api_key

Never commit .env to GitHub.

The repository includes:

.env.example

as a safe configuration template.

▶️ Running the SOC Pipeline

From the project root:

python test_pipeline.py

The pipeline performs:

Detection
    ↓
Threat Intelligence
    ↓
Risk Assessment
    ↓
Security RAG
    ↓
AI Analysis
    ↓
Investigation
    ↓
Response Planning
    ↓
Incident Storage
🌐 Running the Dashboard

Start Flask:

python -m dashboard.app

Then open:

http://127.0.0.1:5000

The dashboard displays:

Current incident
Incident ID
Alert statistics
Risk levels
Threat intelligence
Security knowledge
AI SOC analysis
Response plans
Investigation report
Incident history

A new scan can be triggered from:

/run-scan
🧪 Example Detection

The demo security log contains multiple events.

Example:

Login failed user=admin ip=185.220.101.5

Repeated failed login attempts generate:

Possible Brute Force Attack

Example final risk result:

Threat: Possible Brute Force Attack
Severity: HIGH
Risk Score: 86
Risk Level: CRITICAL

Other demonstrated alerts include:

Sensitive File Access
Port Scanning
Failed Privilege Escalation
📊 Example SOC Output
===== FINAL SOC SUMMARY =====

Total Alerts: 4

Sensitive File Access
Severity: MEDIUM
Risk Score: 25
Risk Level: LOW

Port Scanning
Severity: HIGH
Risk Score: 40
Risk Level: MEDIUM

Failed Privilege Escalation
Severity: HIGH
Risk Score: 40
Risk Level: MEDIUM

Possible Brute Force Attack
Severity: HIGH
Risk Score: 86
Risk Level: CRITICAL
🗃️ Incident Management

Processed SOC incidents are stored locally.

storage/incidents.json

Each incident contains information such as:

Incident ID
Creation timestamp
Alerts
Investigation report
Status

Example:

INC-0004
Status: OPEN
📝 Centralized Logging

The platform maintains application-level logs in:

logs/soc_platform.log

The logger records important pipeline events such as:

SOC pipeline started
Detection completed
Alert processed
Investigation completed
Incident stored
SOC pipeline completed

Errors are also captured for troubleshooting.

🔒 Security Considerations

This project follows several security-oriented practices:

API keys stored in environment variables
.env excluded from Git
Private keys excluded from Git
Generated SOC data excluded from Git
Private IP threat-intelligence lookups skipped
AI instructed not to invent security evidence
AI-generated response treated as recommendations
Potential attack relationships treated as hypotheses
Destructive response actions are not automatically executed
⚠️ Project Scope

This project is an educational and portfolio-oriented SOC platform.

It demonstrates the architecture and workflow of an AI-assisted SOC system using simulated security logs and external threat intelligence.

It should not be considered a replacement for a production SIEM/SOC platform without additional security controls, testing, authentication, scalable storage, monitoring, and operational validation.

🔮 Future Enhancements

Possible future development includes:

Real-time log ingestion
Linux authentication log integration
Windows Event Log integration
SIEM integrations
PostgreSQL / MongoDB incident database
User authentication and RBAC
WebSocket-based live alerts
Advanced embeddings for RAG
Vector database integration
MITRE ATT&CK mapping
Automated alert deduplication
Analyst approval workflow
SOAR integrations
Containerized deployment
Cloud deployment
Production-grade observability
🎓 Learning Outcomes

This project demonstrates practical experience with:

Cybersecurity monitoring
SOC workflows
Security log analysis
Threat intelligence
Risk assessment
LLM integration
Retrieval-Augmented Generation
Multi-agent architecture
Incident management
API integration
Flask development
Git/GitHub
Security-focused application design
👨‍💻 Author

Vishal Soni

B.Tech Information Technology

Cybersecurity | AI Agents | Software Development

⭐ Project

If you find this project useful for learning AI-assisted cybersecurity and SOC architecture, consider starring the repository.

