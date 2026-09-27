import os


def get_release_status():
    environment = os.getenv("APP_ENV", "LOCAL")

    return f"Release Management CI/CD Project is running - Environment: {environment}"


if __name__ == "__main__":
    print(get_release_status())