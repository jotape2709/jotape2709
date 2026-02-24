
<!--
   ██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗
   ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝
   ██████╔╝█████╗  ██║  ██║██║   ██║██████╔╝███████╗
   ██╔══██╗██╔══╝  ██║  ██║██║   ██║██╔═══╝ ╚════██║
   ██║  ██║███████╗██████╔╝╚██████╔╝██║     ███████║
   ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚══════╝
-->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b0b0b,50:1b0000,100:ff1a1a&height=290&section=header&text=JO%C3%83O%20PEDRO&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=RED%20TEAM%20%7C%20PENTEST%20%7C%20RECON%20%7C%20LINUX%20%7C%20NETWORKS&descAlignY=58&descSize=18" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=18&pause=1100&color=FF1A1A&center=true&vCenter=true&width=780&lines=Curiosity+is+a+weapon.;Security+is+an+arms+race.;Recon+%E2%86%92+Exploit+%E2%86%92+Post+%E2%86%92+Report.;Learning%2C+building%2C+breaking%2C+documenting." />
</p>

<p align="center">
  <a href="#pt-br"><b>🇧🇷 PT-BR</b></a> •
  <a href="#en"><b>🇺🇸 EN</b></a> •
  <a href="https://www.linkedin.com/in/joao2709"><b>LinkedIn</b></a> •
  <a href="https://github.com/jotape2709"><b>GitHub</b></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Red%20Team-0b0b0b?style=for-the-badge&logo=protonvpn&logoColor=ff1a1a" />
  <img src="https://img.shields.io/badge/Pentest-0b0b0b?style=for-the-badge&logo=hackthebox&logoColor=ff1a1a" />
  <img src="https://img.shields.io/badge/Linux-0b0b0b?style=for-the-badge&logo=linux&logoColor=ff1a1a" />
  <img src="https://img.shields.io/badge/Python-0b0b0b?style=for-the-badge&logo=python&logoColor=ff1a1a" />
  <img src="https://img.shields.io/badge/Networks-0b0b0b?style=for-the-badge&logo=cisco&logoColor=ff1a1a" />
</p>

---

<a id="pt-br"></a>

## 🟥 OPERATOR PANEL (PT-BR)

```bash
root@redops:~# whoami
joao-pedro

root@redops:~# current_role
Infraestrutura & Redes • Estudante de Segurança da Informação

root@redops:~# objective
Estágio em Segurança (entrada por SOC/SecOps/NetSec → caminho até Red Team)

root@redops:~# focus
Recon • Pentest • Linux • Network Visibility • Automation (Python/Bash)
````

---

## 🧨 Portfolio de Segurança (CINEMATIC MODE)

> **Prova prática > certificado**. Aqui está o que eu construo / estudo / documento.

### ⚡ SwiftScan-ICMP (Recon Toolkit) 〔repo: `lab-test`〕

**ICMP discovery + threading + CIDR + output** — focado em visibilidade e enumeração em rede.

🔗 [https://github.com/jotape2709/lab-test](https://github.com/jotape2709/lab-test)

**O que isso mostra em entrevista**

* redes: subnets/CIDR/discovery
* performance: threading/IO
* engenharia: CLI + organização + output

---

### 🧱 Home Lab (Infra + Security)

* segmentação e testes controlados
* serviços internos e observabilidade
* aprendizado contínuo (logs, detecção, superfície de ataque)

## 🧱 Home Lab Blueprint (Infra + Security) — “REDOPS RANGE”

> Ambiente controlado para simular redes reais, validar hipóteses e treinar **recon → exploração → detecção → hardening**.

### 🗺️ Network Map (High-level)

```mermaid
flowchart LR
  I[Internet] --> R[Router/ISP]
  R --> FW[Firewall/Gateway<br/>pfSense/OPNsense ou FortiGate (lab)]
  FW --> SW[Switch / VLAN Trunk]

  SW --> V10[VLAN 10 • Workstation/Attacker<br/>Kali/Parrot]
  SW --> V20[VLAN 20 • Users/Clients<br/>Windows/Linux]
  SW --> V30[VLAN 30 • Servers/Services<br/>Docker/VMs]
  SW --> V40[VLAN 40 • AD / Identity<br/>DC + Clients]
  SW --> V50[VLAN 50 • Monitoring<br/>SIEM/Logs/NIDS]

  V50 --> SIEM[SIEM / Log Stack<br/>Wazuh/ELK/Splunk Free]
  V50 --> NIDS[NIDS<br/>Suricata/Zeek]
  V30 --> SRV[Services<br/>DNS/Web/Files/DB]
  V40 --> AD[Domain Controller<br/>AD DS + GPO]
---

## 🧠 “Modo recrutador leigo” (explicação simples)

<details>
<summary><b>📌 Clique para abrir</b></summary>

Eu já trabalho com infraestrutura de redes e uso isso para estudar segurança na prática.

**O que eu sei fazer bem:**

* Redes (estrutura física e lógica, troubleshooting)
* Linux (administração) e automação com Python/Bash
* Reconhecimento/enumeração (mapeamento de rede, descoberta de hosts)

**O que eu procuro agora:**

* Estágio em Segurança (SOC/SecOps/Segurança de Redes/Cloud Security)
* Objetivo de longo prazo: Red Team / Pentest

</details>

---

## 🛰️ Telemetry & Activity (NÃO QUEBRA)

<p align="center">
  <img src="./profile-summary-card-output/tokyonight/0-profile-details.svg" />
</p>

<p align="center">
  <img src="./profile-summary-card-output/tokyonight/1-repos-per-language.svg" />
  <img src="./profile-summary-card-output/tokyonight/2-most-commit-language.svg" />
</p>

<p align="center">
  <img src="./profile-summary-card-output/tokyonight/3-stats.svg" />
  <img src="./profile-summary-card-output/tokyonight/4-productive-time.svg" />
</p>

---

## 🐍 Contribution Snake (ANIMADO)

<p align="center">
  <img src="https://github.com/jotape2709/jotape2709/blob/output/github-contribution-grid-snake.svg" />
</p>

---

## 🧬 Attack/Defense HUD

```text
[ Recon ]
Surface mapped → Signals collected → Hypotheses built

[ Exploit ]
Controlled execution → Minimal noise → Objective-focused

[ Report ]
Evidence → Impact → Remediation → Verification
```

---

<a id="en"></a>

## 🟥 Recruiter-friendly (EN)

<details>
<summary><b>Open English version</b></summary>

### Who I am

Infrastructure & Networks background, studying Information Security.

### What I’m aiming for

Internship in Information Security (SOC/SecOps/Network Security/Cloud Security as entry points → long-term Red Team).

### Proof of Work

* SwiftScan-ICMP (ICMP recon toolkit, threading, CIDR support):
  [https://github.com/jotape2709/lab-test](https://github.com/jotape2709/lab-test)

</details>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=jotape2709&color=ff1a1a" />
</p>
```
