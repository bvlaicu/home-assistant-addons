# Home Assistant Add-ons

## About

Home Assistant allows anyone to create add-on repositories to share their
add-ons for Home Assistant easily. This repository is one of those repositories,
providing extra Home Assistant add-ons for your installation.

## Installation

In the Home Assistant add-on store, a possibility to add a repository is provided.

Use the following URL to add this repository:

```txt
https://github.com/bvlaicu/home-assistant-addons
```

## Add-ons provided by this repository


### [Dashcast][addon-dashcast]
Display dashboard web pages on your Chromecast device
### [Meter Reader][addon-meter-reader]
Put a webcam in front of your utility meter and AWS Rekognition sends the reading over MQTT to a MQTT server of your choice
### [MiniDLNA][addon-minidlna]
MiniDLNA server serving web content from the /data persistent volume
### [RTLAMR][addon-rtlamr]
Listen for 433MHz RF transmissions of utility meterss and publish the data via MQTT
### [Oru][addon-oru]
Retrieving the last meter read from Orange and Rockland Utility or ConEdison and publish the data via MQTT
### [PHP][addon-php]
PHP server serving web content from the /data persistent volume

## Releases

Releases are based on [Semantic Versioning][semver], and use the format
of ``MAJOR.MINOR.PATCH``. In a nutshell, the version will be incremented
based on the following:

- ``MAJOR``: Incompatible or major changes.
- ``MINOR``: Backwards-compatible new features and enhancements.
- ``PATCH``: Backwards-compatible bugfixes and package updates.

## Support

Got questions?

You have several options to get them answered:

- The Home Assistant Community Add-ons [Discord Chat Server][discord]
- The Home Assistant [Community Forum][forum].
- The Home Assistant [Discord Chat Server][discord-ha].
- Join the [Reddit subreddit][reddit] in [/r/homeassistant][reddit]

You could also open an issue here on GitHub. Note, we use a separate
GitHub repository for each add-on. Please ensure you are creating the issue
on the correct GitHub repository matching the add-on.

## License

MIT License

Copyright (c) 2019-2020 Bogdan Vlaicu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


[addon-dashcast]: https://github.com/bvlaicu/home-assistant-addons/tree/master/dashcast
[addon-meter-reader]: https://github.com/bvlaicu/home-assistant-addons/tree/master/meter-reader
[addon-minidlna]: https://github.com/bvlaicu/home-assistant-addons/tree/master/minidlna
[addon-rtlamr]: https://github.com/bvlaicu/home-assistant-addons/tree/master/rtlamr
[addon-oru]: https://github.com/bvlaicu/home-assistant-addons/tree/master/oru
[addon-php]: https://github.com/bvlaicu/home-assistant-addons/tree/master/php
