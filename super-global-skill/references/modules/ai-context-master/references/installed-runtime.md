# Runtime discovery — portable

This package contains workflow guidance, not an installed MemoryOS or Context Hub runtime.

1. Use the current shell's executable lookup (or Python `shutil.which`) for `memoryos` and `chub`; on Windows consider `.cmd` shims.
2. Read the discovered executable's help/status before relying on a command or storage location. Use only a runtime configured for the current user and task.
3. If missing, use the project checkpoint for continuity and official docs for lookup. Do not install a runtime or upload source merely to use this module.
4. No credentials, personal memory, vendor workspace or machine-specific paths are shipped in this package.
