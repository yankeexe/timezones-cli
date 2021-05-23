<img src="https://i.imgur.com/ZebplfT.png" width="110" align="left"/><h1>Timezone CLI</h1>

<p>Get local datetime from multiple timezones.</p>

<br>

**All datetimes you care for, at a glance.**

<img src="https://i.imgur.com/JIt8tQN.png"  width="500" />

- [Timezone CLI](#timezone-cli)
  - [Usage](#usage)
    - [Installation](#installation)
    - [Search for local date time](#search-for-local-date-time)
    - [Add timezones](#add-timezones)
    - [Remove timezones](#remove-timezones)
    - [Show local datetime of all saved timezones](#show-local-datetime-of-all-saved-timezones)
    - [Select a single timezone from defaults](#select-a-single-timezone-from-defaults)
    - [Get UTC Time](#get-utc-time)
  - [Contributing](#contributing)

## Usage

### Installation

```bash
  $ pip3 install timezones-cli
```

### Search for local date time

```bash
$ tz search "us"
```

<details><summary><strong>Demo</strong></summary>

<img src = "https://i.imgur.com/D2bcHG2.gif" width="700" alt="demo of timezone cli search" />
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

## Contributing

For guidance on setting up a development environment and how to make a contribution to `timezones-cli`, see the [contributing guidelines](https://github.com/yankeexe/timezones-cli/blob/master/CONTRIBUTING.md).

```

```
