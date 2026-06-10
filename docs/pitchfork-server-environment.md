# Pitchfork Server Environment

## Floating Eye Software Infrastructure Primer

### Status

Living Reference Document

### Audience

* Developers
* Contributors
* Node Operators
* Project Nursery Participants
* Future Community Administrators

---

# Purpose

This document describes the baseline server environment used by Floating Eye Software projects.

It explains the practical infrastructure choices currently used for Pancakes, Pitchfork, Red Witch, Resonance, and related prototype deployments.

The goal is not to prescribe a permanent architecture.

The goal is to establish a simple, understandable, low-cost environment that allows projects to become real software without requiring enterprise-scale infrastructure.

Throughout the ecosystem we generally prefer:

```text
simple
before
clever
```

and:

```text
self-hostable
before
platform-dependent
```

Infrastructure should remain understandable by a technically curious person with basic Linux experience.

---

# Design Philosophy

The Pancakes ecosystem is intentionally designed around the concept of nodes rather than platforms.

A node should be capable of running:

* independently
* on modest hardware
* under local control
* with minimal vendor lock-in

As a result, the preferred deployment environment is intentionally conservative:

```text
Linux
Virtual Machine
SSH
DNS
Backups
```

rather than:

```text
Kubernetes
Cloud-Native Service Meshes
Managed Infrastructure Dependencies
Complex Multi-Region Architectures
```

Those technologies may eventually have a role, but they are not required to build meaningful software.

The ecosystem should remain understandable by ordinary people.

---

# Infrastructure Layers

A typical deployment consists of:

```text
Domain Name
↓
DNS
↓
Public Server
↓
Ubuntu
↓
Application Services
↓
Pancakes / Pitchfork Software
```

Each layer has a distinct responsibility.

---

# Domains

Floating Eye Software typically acquires domains through conventional domain registrars.

Examples include:

```text
floatingeye.net
fley.org
pancakes.ca
pancakes.love
```

Domains provide stable human-readable names for services.

Servers may change.

IP addresses may change.

Domains should remain stable.

Examples:

```text
resonance.floatingeye.net
node.fley.org
mood.fley.org
```

---

# DNS

## Preferred Provider

NearlyFreeSpeech.NET

Historically, Floating Eye Software has used NearlyFreeSpeech.NET for DNS management.

Reasons include:

* simplicity
* reliability
* low cost
* minimal advertising
* long operational history

DNS records map names to servers.

Example:

```text
resonance.floatingeye.net
→
203.0.113.42
```

A user connects to:

```text
resonance.floatingeye.net
```

without needing to know the underlying server address.

---

# DigitalOcean

## Preferred Hosting Provider

DigitalOcean is currently the preferred virtual server provider.

Reasons include:

* simple pricing
* predictable billing
* straightforward virtual machines
* excellent documentation
* easy SSH access
* easy resizing
* minimal operational overhead

DigitalOcean virtual machines are called:

```text
Droplets
```

A Droplet is simply a Linux server running in a data center.

For most Project Nursery work, this is sufficient.

---

# Typical Droplet Sizes

Prototype deployments generally begin small.

### Minimal Prototype

```text
1 vCPU
2 GB RAM
```

Suitable for:

* Flask applications
* Node Lite
* small personal nodes
* experimentation

---

### Comfortable Prototype

```text
1 vCPU
4 GB RAM
```

Suitable for:

* multiple services
* development environments
* Minecraft testing
* small shared nodes

---

### Community Node

```text
2+ vCPU
4+ GB RAM
```

Used when actual users begin participating.

The preferred approach is:

```text
start small
measure
scale later
```

---

# Operating System

## Preferred OS

Ubuntu LTS

Current deployments generally target:

```text
Ubuntu 24.04 LTS
```

or whatever current Ubuntu Long-Term Support release is available.

Reasons:

* large user community
* extensive documentation
* stable upgrade path
* broad package support

Ubuntu forms the foundation of all higher-level services.

---

# Users and Permissions

Servers should not be administered as root during normal operation.

Preferred structure:

```text
root
↓
administrator account
↓
service accounts
```

Examples:

```text
resonance
minecraft
pitchfork
postgres
```

Each service should run under its own account whenever practical.

This limits the impact of configuration mistakes and security failures.

---

# SSH

## Preferred Administration Method

SSH is the primary administration interface.

Typical usage:

```bash
ssh username@server.example.com
```

Preferred practices:

* SSH keys
* disable password authentication
* disable root login
* use sudo when necessary

SSH should be considered the primary administrative boundary of the node.

Protect it accordingly.

---

# Firewalls

## Preferred Firewall

UFW

Ubuntu's Uncomplicated Firewall provides a simple interface for firewall management.

Example:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 25565
sudo ufw enable
```

Only required ports should be exposed.

Common examples:

| Port  | Purpose   |
| ----- | --------- |
| 22    | SSH       |
| 80    | HTTP      |
| 443   | HTTPS     |
| 25565 | Minecraft |

A closed port is generally safer than an open port.

---

# Application Hosting

## Preferred Approach

For early-stage projects, applications should run directly on the server.

Typical stack:

```text
Ubuntu
↓
Python
↓
Gunicorn
↓
Flask
↓
SQLite
```

This is sufficient for:

* Mood Ring
* Node Lite
* prototype APIs
* experimental services

No reverse proxy is required initially.

No containers are required initially.

No orchestration is required initially.

---

# Gunicorn

## Preferred Python Application Server

Gunicorn is the default server for Flask-based applications.

Example:

```bash
gunicorn app:app \
  --bind 0.0.0.0:5000
```

Benefits:

* simple
* stable
* well understood
* lightweight

Applications should generally run under systemd rather than inside terminal sessions.

---

# Systemd

## Preferred Service Manager

Long-running services should be managed through systemd.

Examples:

```text
mood-ring.service
node-lite.service
minecraft.service
```

Benefits:

* automatic startup
* automatic restart
* log integration
* service monitoring

Applications should survive server reboots automatically.

---

# Databases

The ecosystem intentionally prefers simple databases first.

---

## SQLite

Preferred for:

* prototypes
* local-first applications
* personal nodes
* Project Nursery work

Benefits:

* no separate server
* minimal administration
* easy backups
* easy portability

Most early Pitchfork services should begin with SQLite.

---

## PostgreSQL

Preferred when:

* multiple users exist
* concurrency increases
* application complexity grows

PostgreSQL is the likely long-term database platform for larger deployments.

However:

```text
SQLite first.
PostgreSQL when necessary.
```

---

# HTTPS

Public-facing services should eventually use HTTPS.

Typical approach:

```text
Let's Encrypt
+
Certbot
```

HTTPS becomes important once:

* external testers are invited
* authentication exists
* personal data is transmitted

Internal prototypes may initially operate without HTTPS during development.

---

# Nginx

## Future Infrastructure Layer

Nginx is not required for the first generation of deployments.

It becomes useful when:

* multiple web applications exist
* HTTPS termination is needed
* virtual host routing becomes desirable

Example:

```text
mood.fley.org
node.fley.org
api.fley.org
```

may all be routed through a single Nginx instance.

Nginx should be introduced because it solves a real problem, not because tutorials recommend it.

---

# Minecraft Infrastructure

The Resonance server introduces a new class of node:

```text
Ambient World Node
```

Typical stack:

```text
DigitalOcean
↓
Ubuntu
↓
Java
↓
Minecraft Server
```

Initially:

```text
Vanilla Minecraft
```

Later:

```text
Paper Server
```

when plugin support becomes necessary.

The Minecraft server is treated as a Pitchfork client rather than the Pitchfork system itself.

---

# Resonance

The Resonance server is the first planned ambient-world deployment.

Example:

```text
resonance.floatingeye.net
```

Purpose:

* environmental projection
* symbolic world experimentation
* ambient client development
* Pitchfork validation

The Minecraft world acts as an experiential environment rather than a dashboard.

---

# Backups

Backups are mandatory.

Minimum requirements:

* application data
* SQLite databases
* configuration files
* Minecraft worlds

Backups should exist outside the running server.

A server without backups should be considered temporary.

---

# Monitoring

Prototype systems may rely on simple operational tools:

```bash
systemctl status
journalctl
df -h
free -h
top
```

Formal monitoring systems can be added later.

Operational simplicity is generally preferred over premature observability infrastructure.

---

# Logging

Logs should support debugging.

Logs should not become surveillance artifacts.

Projects should avoid logging:

* private notes
* journal content
* health information
* Red Witch data
* sensitive personal records

The ability to debug a system should not require collecting unnecessary personal information.

---

# Node Identity

Within the Pancakes ecosystem, a server is more than a machine.

A node is simultaneously:

* a deployment boundary
* a governance boundary
* a permission boundary
* a trust boundary
* a stewardship boundary

Infrastructure decisions should reflect this principle.

The server exists to support its participants.

Not the other way around.

---

# Preferred Development Progression

New projects should generally evolve in the following order:

```text
Local Development
↓
Single Ubuntu VM
↓
DNS
↓
Gunicorn
↓
Backups
↓
Multiple Services
↓
HTTPS
↓
Nginx
↓
Community Use
↓
Federation
```

Avoid skipping directly to large-scale architecture.

Meaningful software can emerge long before infrastructure becomes sophisticated.

---

# Summary

The Floating Eye Software infrastructure model intentionally favors simplicity.

The preferred stack today is:

```text
Domain Registrar
↓
NearlyFreeSpeech DNS
↓
DigitalOcean Droplet
↓
Ubuntu LTS
↓
SSH
↓
UFW
↓
Systemd
↓
Gunicorn
↓
SQLite
↓
Pancakes / Pitchfork Applications
```

Additional layers such as:

```text
HTTPS
Nginx
PostgreSQL
Containers
Federation
```

can be introduced later when they solve real operational problems.

The objective is not infrastructure sophistication.

The objective is infrastructure that enables humane software to exist.
