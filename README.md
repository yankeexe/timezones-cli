<img src="https://i.imgur.com/ZebplfT.png" width="110" align="left"/><h1>Timezones CLI</h1>

<p>Get local datetime from multiple timezones.</p>
<p>
<img src="https://img.shields.io/pypi/v/timezones-cli?color=%2334D058" />
<img src="https://img.shields.io/pypi/pyversions/timezones-cli?color=%2334D058" />
<img src="https://img.shields.io/pypi/l/timezones-cli?color=%2334D058" />
</p>
<br>

**All datetimes you care for, at a glance.**

<img src="https://i.imgur.com/JIt8tQN.png"  width="500" />

- [Installation](#installation)
- [Usage](#usage)
  - [Search for local date time](#search-for-local-date-time)
  - [Search based on timezone abbreviations](#search-based-on-timezone-abbreviations)
  - [Add timezones](#add-timezones)
  - [Remove timezones](#remove-timezones)
  - [Show local datetime of all saved timezones](#show-local-datetime-of-all-saved-timezones)
  - [Select a single timezone from defaults](#select-a-single-timezone-from-defaults)
  - [Get UTC time](#get-utc-time)
- [Run using Docker :whale:](#run-using-docker-whale)
- [Contributing](#contributing)


## Installation

```bash
  $ pip3 install timezones-cli
```
To run this CLI using Docker, check [Run using Docker :whale:](#run-using-docker-whale).

> **NOTE:** [List of country codes or timezone names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) :earth_asia:

> **Use `-t` flag to toggle 24 hours format.**

## Usage

### Search for local date time

You can use short country code like 'AE', 'RU', 'US' and so on.

You can search via city like: 'Paris', 'London', 'Moscow', 'Chicago' and so on.

```bash
$ tz search "us"

$ tz search "Nepal"

$ tz search "Paris"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/D2bcHG2.gif" width="700" alt="demo of timezone cli search" />
</details>

---

### Search based on timezone abbreviations

```bash
$ tz get "pst"

$ tz get "ist"

$ tz get "est"

$ tz get "cst"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/2xNhV08.gif" width="700" alt="demo of timezone cli search" />
</details>

---

### Add timezones

Timezones added to the config file are treated as the default timezones which is triggered by the `tz show` command.

> file is stored at ~/.tz-cli

```bash
$ tz add "Asia/Kathmandu"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/32XUBIP.gif" width="700" alt="demo of timezone cli add" />
</details>
---

### Remove timezones

There are two ways for removing timezones from the config file. Using the `--interactive` mode and passing the the `--name` flag.

```bash
$ tz remove -i

$ tz remove --name "Asia/Kathmandu"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/q0lRtJt.gif" width="700" alt="demo of timezone cli remove" />
</details>

---

### Show local datetime of all saved timezones

```bash
$ tz show
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/s2Qq1Yb.gif" width="700" alt="demo of timezone cli show" />
</details>
---

### Select a single timezone from defaults

```bash
$ tz select
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/VF91IZE.gif" width="700" alt="demo of timezone cli select" />
</details>

---

### Get UTC time

Get UTC time based on current system time.

> **tz utc --help**

```bash
$ tz utc
```

Get UTC time based on specified time and timezone.

```bash
$ tz utc <time> <timezone>

$ tz utc "11:45PM" "Asia/Kathmandu"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/8hjy1XP.gif" width="500" alt="demo of timezone cli select" />
</details>

## Run using Docker :whale:

```bash
docker pull ghcr.io/yankeexe/timezones-cli:latest
```

Verify signature of the image: requires [cosign](https://docs.sigstore.dev/cosign/installation/).

```bash
COSIGN_EXPERIMENTAL=true cosign verify ghcr.io/yankeexe/timezones-cli:latest
```

Create a config file manually first.

```bash
$ touch ~/.tz-cli

$ docker run --rm -it -v ${HOME}/.tz-cli:/home/tz/.tz-cli ghcr.io/yankeexe/timezones-cli search us
```
For convenience you can add alias of the command to your shell config:
```bash
$ echo "alias tz='docker run --rm -it -v ${HOME}/.tz-cli:/home/tz/.tz-cli ghcr.io/yankeexe/timezones-cli'" >> ~/.bashrc
$ source ~/.bashrc

$ echo "alias tz='docker run --rm -it -v ${HOME}/.tz-cli:/home/tz/.tz-cli ghcr.io/yankeexe/timezones-cli'" >> ~/.zshrc
$ source ~/.zshrc

# Use alias to invoke timezones-cli
$ tz search Nepal
```

---

For local debugging: Use the `make run` command followed by the command you want to run against the `tz` binary.

```bash
$ make run cmd="get ist"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/t8RgJqg.png" width="500" alt="demo of timezone cli with Docker" />
</details>

## Contributing

For guidance on setting up a development environment and how to make a contribution to `timezones-cli`, see the [contributing guidelines](https://github.com/yankeexe/timezones-cli/blob/master/CONTRIBUTING.md).
