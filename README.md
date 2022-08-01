# Repository with all Django homeworks

---

## 🏠 Homework #14

Implemented simple CRUD functionality.

Below will be listed all the homework related actions.

### ▶️ Run

Make all actions needed for run homework from zero.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## 🏗️ Preparation

Make some initialization steps. For example, copy configs.

```shell
make init-configs-i-dev
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏯️ Run extended

Shutdown previous, run in detached mode, follow logs

```shell
make d-run-i-extended
```

### ⏹️Stop

Stop services

```shell
make d-stop
```

### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```

### 🦸Superuser

For creating superuser, please run the following command.

```shell
make init-dev-create-superuser
```

---

## 🗒Useful scripts

### 👥 Create 3 random contacts

The following contacts will be created
with random first names and phone number

```shell
make d-create-contacts-i-3
```

### 🔐 Generate 64-length string

```shell
make d-generate-password-i-64
```

---
