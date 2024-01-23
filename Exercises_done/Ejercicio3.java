package programmingBlind.Level0;

import java.util.Scanner;

public class Ejercicio3 {

	private static final String USERNAME = "user";
	private static final String PASSWORD = "pass";
	private static final int MAX_LOGIN_ATTEMPTS = 3;

	private static final String[] PROGRAMS = { "Computer Science", "Medicine", "Marketing", "Arts" };
	private static final int[] AVAILABLE_SLOTS = { 1, 3, 1, 1 };
	private static final String[] CAMPUSES = { "London", "Manchester", "Liverpool" };

	private static String[] enrolledStudents = new String[4];
	private static int[] slotsRemaining = { 1, 3, 1, 1 };

	private static Scanner scanner = new Scanner(System.in);
	private static int loginAttempts = 0;

	public static void main(String[] args) {
		login();
	}

	private static void login() {
		do {
			System.out.print("Enter username: ");
			String usernameInput = scanner.next();
			System.out.print("Enter password: ");
			String passwordInput = scanner.next();

			if (usernameInput.equals(USERNAME) && passwordInput.equals(PASSWORD)) {
				displayProgramMenu();
				break;
			} else {
				System.out.println("Incorrect login information. Please try again.");
				loginAttempts++;

				if (loginAttempts >= MAX_LOGIN_ATTEMPTS) {
					System.out.println("Too many incorrect login attempts. The system is locked.");
					System.exit(0);
				}
			}
		} while (true);
	}

	private static void displayProgramMenu() {
		System.out.println("Available Programs:");
		for (int i = 0; i < PROGRAMS.length; i++) {
			System.out.println((i + 1) + ". " + PROGRAMS[i] + " - Slots Remaining: " + slotsRemaining[i]);
		}

		System.out.print("Choose a program (1-4): ");
		int programChoice = scanner.nextInt();

		if (programChoice < 1 || programChoice > 4) {
			System.out.println("Invalid program choice. Please choose a valid program.");
			displayProgramMenu();
		}

		enrollStudent(programChoice - 1);
	}

	private static void enrollStudent(int programIndex) {
		if (slotsRemaining[programIndex] > 0) {
			System.out.print("Enter your first name: ");
			String firstName = scanner.next();
			System.out.print("Enter your last name: ");
			String lastName = scanner.next();
			System.out.print("Choose a campus (1-3): ");
			int campusChoice = scanner.nextInt();

			if (campusChoice < 1 || campusChoice > 3) {
				System.out.println("Invalid campus choice. Please choose a valid campus.");
				enrollStudent(programIndex);
			}

			int campusIndex = campusChoice - 1;

			if (slotsRemaining[programIndex] > 0 && campusIndex < CAMPUSES.length && campusIndex >= 0) {
				enrolledStudents[programIndex] = "Name: " + firstName + " " + lastName + ", Program: "
						+ PROGRAMS[programIndex] + ", Campus: " + CAMPUSES[campusIndex];
				slotsRemaining[programIndex]--;
				System.out.println("Enrollment successful!");
			} else {
				System.out.println("Program at this campus is full. Do you want to enroll in another campus? (Y/N)");
				String choice = scanner.next();
				if (choice.equalsIgnoreCase("Y")) {
					displayProgramMenu();
				} else {
					System.out.println("Thank you for using the enrollment system.");
					System.exit(0);
				}
			}
		} else {
			System.out.println("Program is full. Please choose another program.");
			displayProgramMenu();
		}
	}
}
