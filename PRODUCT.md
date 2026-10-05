# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary users are amateur radio operators running a dedicated transmitter
appliance built around a Raspberry Pi and companion radio hardware. They are
technically capable, comfortable with experimental transmission modes, and
willing to use precise controls rather than heavily simplified abstractions.

Their main jobs are to install WsprryPi; configure and operate transmit-only
WSPR, QRSS, FSKCW, and DFCW workflows; select and calibrate transmitter
hardware; review logs and maintenance state; and inspect reception reports.

## Product Purpose

WsprryPi makes a low-cost, low-complexity amateur-radio beacon practical to
install, configure, and operate on common Raspberry Pi hardware. Success means
an operator can move from installation through a correctly configured
transmission, understand the system's current state, and find the detail needed
to diagnose or maintain it.

This repository provides the operator documentation for that product. It
supports task-led learning, installation, configuration, operation,
troubleshooting, and reference workflows.

## Positioning

WsprryPi is a low-cost, self-contained Raspberry Pi transmitter appliance
supporting WSPR plus QRSS, FSKCW, and DFCW through both a web UI and command
line. That combination of appliance-oriented installation, multiple
weak-signal transmission modes, and parallel browser and shell workflows is
the product's distinguishing position.

## Operating Context

Operators use WsprryPi with Raspberry Pi hardware, an appropriate transmitter
backend and radio-frequency filtering, and command-line access through SSH or
a local console. The system may run headless after installation. Normal
configuration and operation happen through the web UI; command-line and INI
workflows remain available for testing, calibration, direct transmissions, and
advanced configuration.

The documentation is written in Markdown, built with Sphinx and the Read the
Docs theme, and published through Read the Docs. It maintains `stable`,
`latest`, and `devel` documentation tracks. Readers commonly move between
procedures, screenshots, configuration tables, command examples, logs,
maintenance controls, reception reports, and troubleshooting material.

## Capabilities and Constraints

- Supported transmission modes are WSPR, QRSS, FSKCW, and DFCW.
- WSPR includes the documented Type 1, Type 2, and Type 3 message workflows.
- WsprryPi supports Raspberry Pi GPIO transmission and documented external
  clock-generator backends, including Si5351-based operation.
- The system is transmit-only; reception reports come from external services
  such as WSPRnet rather than a local receive path.
- Operators must use appropriate radio-frequency filtering. Documentation must
  not imply that unfiltered Raspberry Pi output is safe to transmit.
- WSPR, QRSS, FSKCW, and DFCW are distinct modes. Shared terminology must not
  erase their different timing, message, spacing, and frequency behavior.
- UI labels, configuration keys, accepted values, defaults, units, and
  conditional states must match the implemented product.
- The documentation repository is an independent sibling of the application
  repositories. Generated HTML is validation output and is not an authored
  source of truth.

## Brand Commitments

The product name is **WsprryPi**. Its voice is precise, clean, technical,
direct, and pragmatic. It should feel trustworthy and utilitarian rather than
promotional or decorative. Product language should respect technically
capable operators while keeping installation and routine operation
approachable.

The WsprryPi name, existing logo, real product screenshots, amateur-radio
terminology, and exact visible control labels are established assets and
commitments.

## Evidence on Hand

Available evidence consists of the source repositories, working product
behavior, real web UI screenshots, configuration and command examples,
rendered documentation, and externally observable WSPRnet reception reports.

No testimonials, adoption figures, customer lists, comparative benchmarks, or
general performance claims have been established. Future work must not invent
or imply them.

## Product Principles

1. Prioritize safe, correct transmission and operational clarity.
2. Organize documentation around the operator's task, not the implementation's
   internal structure.
3. Make system state, mode, hardware path, units, and transmission context easy
   to identify.
4. Preserve exact distinctions among WSPR, QRSS, FSKCW, and DFCW behavior.
5. Keep routine workflows approachable while retaining precise advanced and
   command-line reference material.

## Accessibility & Inclusion

Documentation must remain readable, keyboard-accessible, responsive, and
usable by operators who approach computers pragmatically. No specific WCAG
conformance target or additional product-specific accessibility standard has
been established.
