#!/usr/bin/env python3
"""
Multi-LLM Adaptor Registry

Provides factory function to get platform-specific adaptors for skill generation.
Supports Claude AI, Google Gemini, OpenAI ChatGPT, and generic Markdown export.
"""

from typing import Any

from .base import SkillAdaptor, SkillMetadata

# Import adaptors (some may not be implemented yet)
_ClaudeAdaptor: type[SkillAdaptor] | None = None
_GeminiAdaptor: type[SkillAdaptor] | None = None
_OpenAIAdaptor: type[SkillAdaptor] | None = None
_MarkdownAdaptor: type[SkillAdaptor] | None = None

try:
    from .claude import ClaudeAdaptor as _ClaudeAdaptorImport

    _ClaudeAdaptor = _ClaudeAdaptorImport
except ImportError:
    pass

try:
    from .gemini import GeminiAdaptor as _GeminiAdaptorImport

    _GeminiAdaptor = _GeminiAdaptorImport
except ImportError:
    pass

try:
    from .openai import OpenAIAdaptor as _OpenAIAdaptorImport

    _OpenAIAdaptor = _OpenAIAdaptorImport
except ImportError:
    pass

try:
    from .markdown import MarkdownAdaptor as _MarkdownAdaptorImport

    _MarkdownAdaptor = _MarkdownAdaptorImport
except ImportError:
    pass


# Registry of available adaptors
ADAPTORS: dict[str, type[SkillAdaptor]] = {}

# Register adaptors that are implemented
if _ClaudeAdaptor is not None:
    ADAPTORS["claude"] = _ClaudeAdaptor
if _GeminiAdaptor is not None:
    ADAPTORS["gemini"] = _GeminiAdaptor
if _OpenAIAdaptor is not None:
    ADAPTORS["openai"] = _OpenAIAdaptor
if _MarkdownAdaptor is not None:
    ADAPTORS["markdown"] = _MarkdownAdaptor


def get_adaptor(platform: str, config: dict[str, Any] | None = None) -> SkillAdaptor:
    """
    Factory function to get platform-specific adaptor instance.

    Args:
        platform: Platform identifier ('claude', 'gemini', 'openai', 'markdown')
        config: Optional platform-specific configuration

    Returns:
        SkillAdaptor instance for the specified platform

    Raises:
        ValueError: If platform is not supported or not yet implemented

    Examples:
        >>> adaptor = get_adaptor('claude')
        >>> adaptor = get_adaptor('gemini', {'api_version': 'v1beta'})
    """
    if platform not in ADAPTORS:
        available = ", ".join(ADAPTORS.keys())
        if not ADAPTORS:
            raise ValueError(
                f"No adaptors are currently implemented. Platform '{platform}' is not available."
            )
        raise ValueError(
            f"Platform '{platform}' is not supported or not yet implemented. Available platforms: {available}"
        )

    adaptor_class = ADAPTORS[platform]
    return adaptor_class(config)


def list_platforms() -> list[str]:
    """
    List all supported platforms.

    Returns:
        List of platform identifiers

    Examples:
        >>> list_platforms()
        ['claude', 'gemini', 'openai', 'markdown']
    """
    return list(ADAPTORS.keys())


def is_platform_available(platform: str) -> bool:
    """
    Check if a platform adaptor is available.

    Args:
        platform: Platform identifier to check

    Returns:
        True if platform is available

    Examples:
        >>> is_platform_available('claude')
        True
        >>> is_platform_available('unknown')
        False
    """
    return platform in ADAPTORS


# Export public interface
__all__ = [
    "SkillAdaptor",
    "SkillMetadata",
    "get_adaptor",
    "list_platforms",
    "is_platform_available",
    "ADAPTORS",
]
