from elements.button_element import Button
from elements.input_element import Input
from elements.text_element import Text
from components.base_component import BaseComponent
import allure

class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.delete_button = lambda index: Button(
            page,
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button",
            "Delete Exercise",
        )

        self.subtitle = lambda index: Text(
            page,
            f"create-course-exercise-{index}-box-toolbar-subtitle-text",
            f"Exercise #{index + 1} Subtitle",
        )

        self.title_input = lambda index: Input(
            page,
            f"create-course-exercise-form-title-{index}-input",
            f"Exercise #{index + 1} Title",
        )
        self.description_input = lambda index: Input(
            page,
            f"create-course-exercise-form-description-{index}-input",
            f"Exercise #{index + 1} Description",
        )

    def click_delete_button(self, index: int):
        self.delete_button(index).click()

    @allure.step('Check visible create course exercise form at index "{index}"')
    def check_visible(self, index: int, title: str, description: str):
        self.subtitle(index).check_visible()
        self.subtitle(index).check_have_text(f"#{index + 1} Exercise")

        self.title_input(index).check_visible()
        self.title_input(index).check_have_value(title)

        self.description_input(index).check_visible()
        self.description_input(index).check_have_value(description)

    @allure.step('Fill create course exercise form at index "{index}"')
    def fill(self, index: int, title: str, description: str):
        self.title_input(index).fill(title)
        self.description_input(index).fill(description)
