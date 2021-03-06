"""
Tests the port toggle in SONiC.
"""

import pytest

from tests.common import port_toggle


pytestmark = [
    pytest.mark.topology("any")
]


class TestPortToggle(object):
    """
    TestPortToggle class for testing port toggle
    """

    def test_port_toggle(self, duthosts, rand_one_dut_hostname, bring_up_dut_interfaces):
        """
        Validates that port toggle works as expected

        Test steps:
            1.) Flap all interfaces on DUT one by one.
            2.) Verify interfaces are up correctly.

        Pass Criteria: All interfaces are up correctly.
        """
        duthost = duthosts[rand_one_dut_hostname]
        port_toggle(duthost)
