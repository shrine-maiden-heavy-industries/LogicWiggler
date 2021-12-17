# SPDX-License-Identifier: BSD-3-Clause
from .rev1 import WigglerRev1

__all__ = (
	'WigglerRev1',

	'AVAILABLE_PLATFORMS',
)

AVAILABLE_PLATFORMS = {
	'rev1': WigglerRev1,
}
