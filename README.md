<img src="https://i.imgur.com/ZebplfT.png" width="110" align="left"/><h1>Timezones CLI</h1>

<p><strong>CLI toolkit for timezones:zap:</strong></p>
<p>
<img src="https://img.shields.io/pypi/v/timezones-cli?style=flat-square&color=black"/>
<img src="https://img.shields.io/pypi/pyversions/timezones-cli?style=flat-square&color=black"/>
<img src="https://img.shields.io/pypi/l/timezones-cli?style=flat-square&color=black"/>
<img src="https://static.pepy.tech/badge/timezones-cli"/>
</p>


<img src="https://i.imgur.com/JIt8tQN.png"  width="500" />

## What can you do with `timezones-cli`? :sparkles:
- Search for date and time based on city, country, or timezones.
- Manage dashboard for timezones you frequently view.
- Get UTC date and time based on your local timezone or any timezones.

## Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Search for timezones](#search-for-timezones)
  - [Add/save timezones](#addsave-timezones)
  - [Remove timezones](#remove-timezones)
  - [Show saved timezones](#show-saved-timezones)
  - [Select individual timezones from saved](#select-individual-timezones-from-saved)
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

### Search for timezones

Get time based on the entered timezone or country code

- using country code (either 2 or 3 letters):

  ```bash
    $ tz search US

    $ tz search USA
  ```

- using timezone:
  ```bash
    $ tz search Asia/Kathmandu
  ```

- using fuzzy text: (example: Ireland)
  ```bash
    $ tz search Irela
  ```

- using timezone shortcodes (--zone or -z flag):
  ```bash
    $ tz search pst -z

    $ tz search ist -z

    $ tz search jst -z

    $ tz search cest -z

    $ tz search +0543 -z

    $ tz search +05 -z
  ```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/D2bcHG2.gif" width="700" alt="demo of timezone cli search" />
</details>

---

### Add/save timezones

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

### Show saved timezones

```bash
$ tz show
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/s2Qq1Yb.gif" width="700" alt="demo of timezone cli show" />
</details>
---

### Select individual timezones from saved

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
