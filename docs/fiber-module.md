# Fiber module

Field helpers that do not need a network.

## Color code

TIA-598 12-color sequence, wrapping every dozen fibers. Tube/group
color uses the same sequence.

```
eden colors --fiber 37
# Fiber 37: tube Green / fiber Blue
```

## Loss budget

Planning defaults:

- 1310 nm → 0.35 dB/km
- 1550 nm → 0.25 dB/km
- 1625 nm → 0.28 dB/km
- connector 0.50 dB
- splice 0.10 dB
- safety margin 2.00 dB

Override when the design package says otherwise.

```
eden loss --km 12.4 --nm 1550 --connectors 2 --splices 8
```

## Closeout checklist

Generic. Not Zayo, not Charter, not "the packet your PM emails at 6pm."
Use it when you need a list that still works on paper.

Productized workflow with mandatory photos, GPS, and carrier-shaped
packets lives at https://spliceflow.app.
