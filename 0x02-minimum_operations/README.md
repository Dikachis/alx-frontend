# 0x02. Minimum Operations


General Requirements
- Allowed editors: **vi**, **vim**, **emacs**
- All files is interpreted/compiled on ``Ubuntu 14.04 LTS`` using ``python3 (version 3.4.3)``
- The first line of all files is exactly ``#!/usr/bin/python3``
- Code use the ``PEP 8 style (version 1.7.x)``

## Task0:
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

    * Prototype: ``def minOperations(n)``
    * Returns an integer
    * If ``n`` is impossible to achieve, return ``0``

**Example:**

``n = 9``

H => ``Copy All`` => ``Paste`` => HH => ``Paste`` =>HHH => ``Copy All`` => ``Paste`` => HHHHHH => ``Paste`` => HHHHHHHHH

``Number of operations: 6``
