"""
Transmitter for Blackboard content metadata
"""

from integrated_channels.blackboard.client import BlackboardAPIClient
from integrated_channels.integrated_channel.transmitters.content_metadata import ContentMetadataTransmitter


class BlackboardContentMetadataTransmitter(ContentMetadataTransmitter):
    """
    This transmitter transmits exported content metadata to Canvas.
    """

    def __init__(self, enterprise_configuration, client=BlackboardAPIClient):
        """
        Use the ``BlackboardAPIClient`` for content metadata transmission.
        """
        super(BlackboardContentMetadataTransmitter, self).__init__(
            enterprise_configuration=enterprise_configuration,
            client=client
        )
