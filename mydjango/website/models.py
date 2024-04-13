from django.db import models

class Candidate(models.Model):
    """
    Represents a candidate for a position.

    Attributes:
        name (str): The name of the candidate.
        position (str): The position the candidate is running for.
        bio (str): A brief biography of the candidate.
    """

    name = models.CharField(max_length=100, help_text="The name of the candidate.")
    position = models.CharField(max_length=100, help_text="The position the candidate is running for.")
    bio = models.TextField(help_text="A brief biography of the candidate.")

    def __str__(self):
        """
        Returns a string representation of the candidate.

        Returns:
            str: The name of the candidate.
        """
        return self.name

