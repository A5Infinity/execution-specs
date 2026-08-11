"""
The Bogota fork ([EIP-8081]) is the development fork after Amsterdam. It
carries no protocol changes yet: EIPs targeting it are prototyped on their
own branches and land here once accepted.

### Changes

- [EIP-8131: Unified Transaction Content Floor][EIP-8131]

### Releases

[EIP-8081]: https://eips.ethereum.org/EIPS/eip-8081
[EIP-8131]: https://eips.ethereum.org/EIPS/eip-8131
"""

from ethereum.fork_criteria import ForkCriteria, Unscheduled

FORK_CRITERIA: ForkCriteria = Unscheduled(order_index=4)
