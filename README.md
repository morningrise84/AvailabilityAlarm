# AvailabilityAlarm

A simple script to keep checking the stock availability from warehouse. 

## Status

Currently (May 2022) the script works like a charm: I will not maintain the code over time though.

## How it works

It basically keep reloading the buying options until it finds a listing from the warehouse.
Once it finds one, an alarm plays to notify the user.

## How to use

All you need to do before running this script is:
1) provide the path to Chromedriver
2) provide the link to the product you are monitoring
3) provide the path to the alarm sound you want to play (I use one from YouTube library)

## Pro tip

Run the script from a VM located in the same area of the store, in order to reduce the latency
