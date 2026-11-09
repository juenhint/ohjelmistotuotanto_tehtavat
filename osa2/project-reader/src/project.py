class Project:
    def __init__(self, name, description, licence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.licence = licence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n".join(f"- {dep}" for dep in dependencies) if len(dependencies) > 0 else "-"

    def _stringify_authors(self, authors):
        return "\n".join([f"- {author['name']}" for author in authors]) if len(authors) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.licence or '-'}"
            "\n"
            f"\nAuthors:\n{self._stringify_authors(self.authors)}"
            "\n"
            f"\nDependencies:\n{self._stringify_dependencies(self.dependencies)}"
            "\n"
            f"\nDevelopment dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
