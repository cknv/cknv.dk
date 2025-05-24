+++
title = "Resume"
+++
## Common Tenets
**Tests**: if a given behaviour is not encoded into a test it might get inadventently removed by any given change, even something as trivial as a dependency update can change behaviour and with enough distinct integrations _someone_ will be depending on exactly that behaviour.
When changing existing behaviour test-driven development is often a good approach - especially when existing tests makes sure existing behaviours remain.

**Build Engineering**: tests, formatters, linters, and build artifacts should all be scripted and then automated to avoid time wasted on manual processes.
If possible the checks should be codified, so there is no difference between the checks done on each developers local machine and the checks done as a part of or before building a release.

**Reproduceability**: releasing a small fix for a bug should _only_ affect that bug, and should not have any other changes included by accident.
This means that dependencies should be locked and unless explicitly updated should not be updated at all - of course this also means that actually updating dependencies should be so a trivial task that it can be done as downtime between other tasks.

## Backend Developer at OnlineCity
_2019 - present_

Working on improving and maintaining mobile message gateway: GatewayAPI.
- Rewrite older C++ software in modern python.
- Centralize a myriad of microservices into something more suitable for the team.

## Backend Developer at Visma e-conomic
_2018 - 2019_

Developed systems to read and categorize receipt and billing data based on ORC and ML.

- First foray into deploying services on Kubernetes.
- Wrote some auxillary services using Go.

## Python Developer at Falcon.io
_2013 - 2018_

Designed and built the backend for an entire "Social Listening" product slice of the Social Media Managent.

Iterated through three major versions of the product:
- Ad-hoc batch processing system.
- Map/Reduce based on Riak.
- Near-realtime search based on Elasticsearch.

The final version supported just in time query refinement, and a dedicated query language capable of having complex nested queries with many different filters and clauses.
This query language was parsed into an AST for further manipulation (such as optimizations) and then compiled into various forms of queries to either match in Elasticsearch or gather data from many different sources.

## Backend Developer at Art of Crime
_2012 - 2013_

Build game server and auxilary services (such as translation) for the game.
