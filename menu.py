# ================================================================
# COMMUNITY RUNNING EVENT REGISTRATION SYSTEM
# Based on concepts from:
# Problem Solving and Programming Concepts, Ninth Edition
# By Maureen Sprankle and Jim Hubbard
# ================================================================

import datetime

# ============================================================
# CONSTANTS - Textbook Chapter 2, pg 25
# ============================================================
# Constants are values that never change during processing
# Named constants use ALL UPPER-CASE (Chapter 2, pg 26)

BASEFEE_5KM = 80
BASEFEE_10KM = 120
BASEFEE_HALFMARATHON = 200
BASEFEE_MARATHON = 350

DISCOUNT_UNDER18 = 0.15
DISCOUNT_CLUBMEMBER = 0.10
DISCOUNT_SENIOR = 0.20
DISCOUNT_EARLYBIRD = 0.10

MINIMUM_AGE_5KM = 8
MINIMUM_AGE_10KM = 14
MINIMUM_AGE_HALFMARATHON = 16
MINIMUM_AGE_MARATHON = 20

EVENT_DATE = "2026-08-30"
EARLYBIRD_DAYS = 30


# ============================================================
# RUNNER CLASS - Record Structure (Chapter 10, pg 268)
# ============================================================
# A record contains information pertaining to one entity in the file
# Each record is divided into fields (Chapter 10, pg 268)

class Runner:
    """Runner Record Structure - Textbook Chapter 10"""
    
    def __init__(self, race_number, runner_name, age, gender, contact_number,
                 email_address, emergency_contact, race_distance, club_member,
                 registration_date, age_category, base_fee, highest_discount, final_fee):
        
        self.RaceNumber = race_number
        self.RunnerName = runner_name
        self.Age = age
        self.Gender = gender
        self.ContactNumber = contact_number
        self.EmailAddress = email_address
        self.EmergencyContact = emergency_contact
        self.RaceDistance = race_distance
        self.ClubMember = club_member
        self.RegistrationDate = registration_date
        self.AgeCategory = age_category
        self.BaseFee = base_fee
        self.HighestDiscount = highest_discount
        self.DiscountAmount = base_fee * highest_discount
        self.FinalFee = final_fee


# ============================================================
# REGISTRATION SYSTEM CLASS
# ============================================================

class RegistrationSystem:
    
    def __init__(self):
        self.choice = 0
        self.runners = []  # Array to store runner records (Chapter 8, pg 188)
        self.total_income = 0
        self.next_race_number = 1000
        
        # ============================================================
        # SAMPLE USER - One runner pre-loaded (Test Data)
        # ============================================================
        self.create_sample_user()
    
    # ============================================================
    # SAMPLE USER - Textbook Chapter 3: Testing the Solution
    # ============================================================
    # Test data is a set of values for the input data used to check
    # the correctness of the solution (Chapter 3, pg 73)
    # ============================================================
    
    def create_sample_user(self):
        """Create one sample runner for demonstration"""
        
        # Sample runner data
        runner_name = "John Smith"
        age = 25
        gender = "M"
        contact_number = "0821234567"
        email_address = "john.smith@email.com"
        emergency_contact = "Jane Smith - 0827654321"
        race_distance = 21
        club_member = True
        registration_date = "2026-07-25"
        
        # Process the registration
        self.next_race_number += 1
        race_number = self.next_race_number
        
        age_category = self.determine_age_category(age)
        base_fee, highest_discount, discount_amount, final_fee = self.calculate_final_fee(
            race_distance, age, club_member, registration_date
        )
        
        # Create and store runner record
        runner = Runner(
            race_number, runner_name, age, gender, contact_number,
            email_address, emergency_contact, race_distance, club_member,
            registration_date, age_category, base_fee, highest_discount, final_fee
        )
        
        self.runners.append(runner)
        self.total_income += final_fee
        
        print("\n   Sample user created: John Smith (Race #1001)")
    
    # ============================================================
    # DISPLAY MENU - Textbook Chapter 3: Organizing the Solution
    # ============================================================
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*58)
        print("      COMMUNITY RUNNING EVENT REGISTRATION SYSTEM")
        print("="*58)
        print("")
        print("   1. Register a Runner")
        print("   2. Search for a Runner")
        print("   3. Update Runner Information")
        print("   4. Delete a Runner")
        print("   5. Display All Runners")
        print("   6. Generate Reports")
        print("   7. Exit System")
        print("")
        print("="*58)
    
    # ============================================================
    # DECISION STRUCTURES - Textbook Chapter 6
    # ============================================================
    
    def determine_age_category(self, age):
        """
        Determine Age Category - Textbook Chapter 6: Positive Logic
        Tests True conditions first (Chapter 6, pg 115)
        """
        if age >= 60:
            return "Senior"
        elif age >= 40:
            return "Veteran"
        elif age >= 18:
            return "Open"
        else:
            return "Junior"
    
    def determine_base_fee(self, race_distance):
        """Determine Base Fee - Textbook Chapter 6: Decision Structure"""
        if race_distance == 5:
            return BASEFEE_5KM
        elif race_distance == 10:
            return BASEFEE_10KM
        elif race_distance == 21:
            return BASEFEE_HALFMARATHON
        elif race_distance == 42:
            return BASEFEE_MARATHON
        else:
            return 0
    
    def determine_highest_discount(self, age, club_member, registration_date):
        """
        Determine Highest Discount - Textbook Chapter 6
        Only the highest applicable discount is applied
        """
        # Calculate days before event
        reg_date = datetime.datetime.strptime(registration_date, "%Y-%m-%d")
        event_date = datetime.datetime.strptime(EVENT_DATE, "%Y-%m-%d")
        days_before = (event_date - reg_date).days
        
        highest_discount = 0
        
        # Senior discount (20%) - highest priority
        if age >= 60:
            highest_discount = DISCOUNT_SENIOR
        
        # Under 18 discount (15%)
        elif age < 18:
            highest_discount = DISCOUNT_UNDER18
        
        # Club member discount (10%)
        if club_member:
            if highest_discount < DISCOUNT_CLUBMEMBER:
                highest_discount = DISCOUNT_CLUBMEMBER
        
        # Early-bird discount (10%)
        if days_before >= EARLYBIRD_DAYS:
            if highest_discount < DISCOUNT_EARLYBIRD:
                highest_discount = DISCOUNT_EARLYBIRD
        
        return highest_discount
    
    def calculate_final_fee(self, race_distance, age, club_member, registration_date):
        """
        Calculate Final Fee - Textbook Chapter 2: Expressions and Equations
        Formula: FinalFee = BaseFee * (1 - HighestDiscount)
        """
        base_fee = self.determine_base_fee(race_distance)
        highest_discount = self.determine_highest_discount(age, club_member, registration_date)
        discount_amount = base_fee * highest_discount
        final_fee = base_fee - discount_amount
        
        return base_fee, highest_discount, discount_amount, final_fee
    
    def validate_age_eligibility(self, age, race_distance):
        """Validate Age Eligibility - Textbook Chapter 6: Decision Logic"""
        if race_distance == 5:
            return age >= MINIMUM_AGE_5KM
        elif race_distance == 10:
            return age >= MINIMUM_AGE_10KM
        elif race_distance == 21:
            return age >= MINIMUM_AGE_HALFMARATHON
        elif race_distance == 42:
            return age >= MINIMUM_AGE_MARATHON
        else:
            return False
    
    # ============================================================
    # CONTROL MODULE - Textbook Chapter 4, pg 87
    # ============================================================
    
    def run(self):
        """
        Control Module - Controls flow to all other modules
        Uses While/WhileEnd loop (Chapter 7) and Case logic (Chapter 6)
        """
        choice = 0  # Primer Read - Chapter 19, pg 395
        
        while choice != 7:  # While/WhileEnd loop - Chapter 7, pg 146
            
            self.display_menu()
            
            # Input validation - Repeat/Until pattern (Chapter 7, pg 148)
            while True:
                try:
                    choice = int(input("Enter your choice (1-7): "))
                    if 1 <= choice <= 7:
                        break
                    else:
                        print("   Invalid choice. Please enter 1-7.")
                except ValueError:
                    print("   Invalid input. Please enter a number.")
            
            # Case logic structure - Chapter 6, pg 147-148
            if choice == 1:
                self.register_runner()
            elif choice == 2:
                self.search_runner()
            elif choice == 3:
                self.update_runner()
            elif choice == 4:
                self.delete_runner()
            elif choice == 5:
                self.display_all_runners()
            elif choice == 6:
                self.generate_reports()
            elif choice == 7:
                print("\n   Exiting System... Goodbye!")
    
    # ============================================================
    # DISPLAY FUNCTIONS
    # ============================================================
    
    def display_runner_details(self, index):
        """Display individual runner details"""
        runner = self.runners[index]
        print("\n" + "="*58)
        print("                  RUNNER DETAILS")
        print("="*58)
        print(f"   Race Number: {runner.RaceNumber}")
        print(f"   Name: {runner.RunnerName}")
        print(f"   Age: {runner.Age}")
        print(f"   Gender: {runner.Gender}")
        print(f"   Contact: {runner.ContactNumber}")
        print(f"   Email: {runner.EmailAddress}")
        print(f"   Emergency: {runner.EmergencyContact}")
        print(f"   Race Distance: {runner.RaceDistance} km")
        print(f"   Club Member: {'Yes' if runner.ClubMember else 'No'}")
        print(f"   Age Category: {runner.AgeCategory}")
        print(f"   Base Fee: R{runner.BaseFee:.2f}")
        print(f"   Discount: {runner.HighestDiscount*100:.0f}%")
        print(f"   Discount Amount: R{runner.DiscountAmount:.2f}")
        print(f"   Final Fee: R{runner.FinalFee:.2f}")
        print("="*58)
    
    # ============================================================
    # PROCESS MODULES - Textbook Chapter 4, pg 87
    # ============================================================
    
    def register_runner(self):
        """Process module - Register a runner"""
        print("\n" + "="*58)
        print("                   REGISTER RUNNER")
        print("="*58)
        
        # Input validation loops - Repeat/Until pattern (Chapter 7, pg 148)
        runner_name = input("   Name and Surname: ")
        
        while True:
            try:
                age = int(input("   Age: "))
                if age >= 8:
                    break
                else:
                    print("   Age must be at least 8 years old.")
            except ValueError:
                print("   Invalid input. Please enter a number.")
        
        while True:
            gender = input("   Gender (M/F): ").upper()
            if gender in ["M", "F"]:
                break
            else:
                print("   Invalid gender. Enter M or F.")
        
        contact_number = input("   Contact Number: ")
        email_address = input("   Email Address: ")
        emergency_contact = input("   Emergency Contact: ")
        
        while True:
            try:
                race_distance = int(input("   Race Distance (5/10/21/42): "))
                if race_distance in [5, 10, 21, 42]:
                    break
                else:
                    print("   Invalid distance. Choose 5, 10, 21, or 42.")
            except ValueError:
                print("   Invalid input. Please enter a number.")
        
        while True:
            club_member_input = input("   Club Member (Y/N): ").upper()
            if club_member_input in ["Y", "N"]:
                club_member = (club_member_input == "Y")
                break
            else:
                print("   Invalid input. Enter Y or N.")
        
        # Validate age eligibility - Decision Structure
        if not self.validate_age_eligibility(age, race_distance):
            print("\n   Registration Failed. Age not eligible for selected distance.")
            return
        
        registration_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Process registration - Sequential logic (Chapter 5)
        age_category = self.determine_age_category(age)
        base_fee, highest_discount, discount_amount, final_fee = self.calculate_final_fee(
            race_distance, age, club_member, registration_date
        )
        
        # Incrementing - Textbook Chapter 7, pg 145
        self.next_race_number += 1
        race_number = self.next_race_number
        
        # Store record - Textbook Chapter 8: Arrays
        runner = Runner(
            race_number, runner_name, age, gender, contact_number,
            email_address, emergency_contact, race_distance, club_member,
            registration_date, age_category, base_fee, highest_discount, final_fee
        )
        self.runners.append(runner)
        self.total_income += final_fee  # Accumulating - Chapter 7, pg 145
        
        print("\n" + "="*58)
        print("              REGISTRATION SUCCESSFUL!")
        print("="*58)
        print(f"   Race Number: {race_number}")
        print(f"   Age Category: {age_category}")
        print(f"   Base Fee: R{base_fee:.2f}")
        print(f"   Discount Applied: {highest_discount*100:.0f}%")
        print(f"   Discount Amount: R{discount_amount:.2f}")
        print(f"   Final Fee: R{final_fee:.2f}")
        print("="*58)
        input("\n   Press Enter to continue...")
    
    def search_runner(self):
        """Process module - Search for a runner"""
        print("\n" + "="*58)
        print("                    SEARCH RUNNER")
        print("="*58)
        
        if len(self.runners) == 0:
            print("\n   No runners registered.")
            input("   Press Enter to continue...")
            return
        
        print("\n   Search by:")
        print("   1. Race Number")
        print("   2. Runner Name")
        
        while True:
            try:
                search_type = int(input("   Enter choice (1-2): "))
                if search_type in [1, 2]:
                    break
                else:
                    print("   Invalid choice. Enter 1 or 2.")
            except ValueError:
                print("   Invalid input. Please enter a number.")
        
        found = False
        runner_index = -1
        
        # Sequential Search - Textbook Chapter 8, Figure 8.16
        if search_type == 1:
            try:
                search_number = int(input("   Enter Race Number: "))
                i = 0
                while i < len(self.runners) and not found:
                    if self.runners[i].RaceNumber == search_number:
                        found = True
                        runner_index = i
                    i += 1
            except ValueError:
                print("   Invalid input.")
                return
        else:
            search_name = input("   Enter Runner Name: ")
            i = 0
            while i < len(self.runners) and not found:
                if self.runners[i].RunnerName.lower() == search_name.lower():
                    found = True
                    runner_index = i
                i += 1
        
        if found:
            self.display_runner_details(runner_index)
        else:
            print("\n   Runner not found.")
        
        input("\n   Press Enter to continue...")
    
    def update_runner(self):
        """Process module - Update runner information"""
        print("\n" + "="*58)
        print("                  UPDATE RUNNER")
        print("="*58)
        
        if len(self.runners) == 0:
            print("\n   No runners registered.")
            input("   Press Enter to continue...")
            return
        
        try:
            search_number = int(input("   Enter Race Number to update: "))
        except ValueError:
            print("   Invalid input.")
            return
        
        found = False
        runner_index = -1
        
        i = 0
        while i < len(self.runners) and not found:
            if self.runners[i].RaceNumber == search_number:
                found = True
                runner_index = i
            i += 1
        
        if not found:
            print("\n   Runner not found.")
            input("   Press Enter to continue...")
            return
        
        self.display_runner_details(runner_index)
        
        runner = self.runners[runner_index]
        
        print("\n   Enter new details (leave blank to keep current):")
        print("   " + "-"*40)
        
        new_name = input(f"   Name ({runner.RunnerName}): ")
        if new_name:
            runner.RunnerName = new_name
        
        new_age = input(f"   Age ({runner.Age}): ")
        if new_age:
            try:
                runner.Age = int(new_age)
            except ValueError:
                print("   Invalid age. Keeping current.")
        
        new_gender = input(f"   Gender ({runner.Gender}): ").upper()
        if new_gender in ["M", "F"]:
            runner.Gender = new_gender
        
        new_contact = input(f"   Contact Number ({runner.ContactNumber}): ")
        if new_contact:
            runner.ContactNumber = new_contact
        
        new_email = input(f"   Email Address ({runner.EmailAddress}): ")
        if new_email:
            runner.EmailAddress = new_email
        
        new_emergency = input(f"   Emergency Contact ({runner.EmergencyContact}): ")
        if new_emergency:
            runner.EmergencyContact = new_emergency
        
        new_race_distance = input(f"   Race Distance ({runner.RaceDistance}): ")
        if new_race_distance:
            try:
                race_distance = int(new_race_distance)
                if race_distance in [5, 10, 21, 42]:
                    runner.RaceDistance = race_distance
                    base_fee, discount, discount_amt, final_fee = self.calculate_final_fee(
                        runner.RaceDistance, runner.Age, runner.ClubMember, runner.RegistrationDate
                    )
                    runner.BaseFee = base_fee
                    runner.HighestDiscount = discount
                    runner.DiscountAmount = discount_amt
                    runner.FinalFee = final_fee
            except ValueError:
                print("   Invalid distance. Keeping current.")
        
        new_club = input(f"   Club Member (Y/N) ({'Y' if runner.ClubMember else 'N'}): ").upper()
        if new_club in ["Y", "N"]:
            runner.ClubMember = (new_club == "Y")
            base_fee, discount, discount_amt, final_fee = self.calculate_final_fee(
                runner.RaceDistance, runner.Age, runner.ClubMember, runner.RegistrationDate
            )
            runner.BaseFee = base_fee
            runner.HighestDiscount = discount
            runner.DiscountAmount = discount_amt
            runner.FinalFee = final_fee
        
        print("\n   Update Successful!")
        input("   Press Enter to continue...")
    
    def delete_runner(self):
        """Process module - Delete a runner"""
        print("\n" + "="*58)
        print("                  DELETE RUNNER")
        print("="*58)
        
        if len(self.runners) == 0:
            print("\n   No runners registered.")
            input("   Press Enter to continue...")
            return
        
        try:
            search_number = int(input("   Enter Race Number to delete: "))
        except ValueError:
            print("   Invalid input.")
            return
        
        found = False
        runner_index = -1
        
        i = 0
        while i < len(self.runners) and not found:
            if self.runners[i].RaceNumber == search_number:
                found = True
                runner_index = i
            i += 1
        
        if not found:
            print("\n   Runner not found.")
            input("   Press Enter to continue...")
            return
        
        self.display_runner_details(runner_index)
        
        while True:
            confirm = input("\n   Are you sure you want to delete this runner? (Y/N): ").upper()
            if confirm in ["Y", "N"]:
                break
            else:
                print("   Invalid input. Enter Y or N.")
        
        if confirm == "Y":
            deleted_runner = self.runners.pop(runner_index)
            print(f"\n   Runner {deleted_runner.RunnerName} has been deleted.")
        else:
            print("\n   Deletion cancelled.")
        
        input("   Press Enter to continue...")
    
    def display_all_runners(self):
        """Process module - Display all runners"""
        print("\n" + "="*58)
        print("                  ALL RUNNERS")
        print("="*58)
        
        if len(self.runners) == 0:
            print("\n   No runners registered.")
            input("   Press Enter to continue...")
            return
        
        print("\n" + "-"*58)
        print(f"{'Race #':<8} {'Name':<20} {'Age':<6} {'Distance':<10} {'Fee':<8}")
        print("-"*58)
        
        # Automatic-counter loop - Textbook Chapter 7
        for runner in self.runners:
            print(f"{runner.RaceNumber:<8} {runner.RunnerName:<20} {runner.Age:<6} {runner.RaceDistance:<10} R{runner.FinalFee:.2f}")
        
        print("-"*58)
        print(f"\n   Total Runners: {len(self.runners)}")
        print(f"   Total Income: R{self.total_income:.2f}")
        input("\n   Press Enter to continue...")
    
    def generate_reports(self):
        """Process module - Generate reports"""
        print("\n" + "="*58)
        print("                  GENERATE REPORTS")
        print("="*58)
        
        if len(self.runners) == 0:
            print("\n   No runners registered.")
            input("   Press Enter to continue...")
            return
        
        print("\n   1. Runner List Report")
        print("   2. Age Category Report")
        print("   3. Discount Report")
        print("   4. Income Report")
        print("   5. Return to Main Menu")
        
        while True:
            try:
                report_choice = int(input("\n   Enter choice (1-5): "))
                if 1 <= report_choice <= 5:
                    break
                else:
                    print("   Invalid choice. Enter 1-5.")
            except ValueError:
                print("   Invalid input. Please enter a number.")
        
        if report_choice == 1:
            self.runner_list_report()
        elif report_choice == 2:
            self.age_category_report()
        elif report_choice == 3:
            self.discount_report()
        elif report_choice == 4:
            self.income_report()
        elif report_choice == 5:
            return
        
        input("   Press Enter to continue...")
    
    # ============================================================
    # REPORT MODULES - Textbook Chapter 19: Designing Output Reports
    # ============================================================
    
    def runner_list_report(self):
        """Runner List Report - Textbook Chapter 19"""
        print("\n" + "="*58)
        print("                  RUNNER LIST REPORT")
        print("="*58)
        print(f"   Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*58)
        
        print("\n" + "-"*58)
        print(f"{'Race #':<8} {'Name':<20} {'Age':<6} {'Category':<12} {'Distance':<10} {'Fee':<8}")
        print("-"*58)
        
        for runner in self.runners:
            print(f"{runner.RaceNumber:<8} {runner.RunnerName:<20} {runner.Age:<6} {runner.AgeCategory:<12} {runner.RaceDistance:<10} R{runner.FinalFee:.2f}")
        
        print("-"*58)
        print(f"\n   Total Runners: {len(self.runners)}")
        print(f"   Total Income: R{self.total_income:.2f}")
    
    def age_category_report(self):
        """Age Category Report - Textbook Chapter 8: Frequency Distribution"""
        print("\n" + "="*58)
        print("                  AGE CATEGORY REPORT")
        print("="*58)
        print(f"   Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*58)
        
        # Frequency distribution - Textbook Chapter 8, Figure 8.18
        categories = {"Junior": 0, "Open": 0, "Veteran": 0, "Senior": 0}
        
        for runner in self.runners:
            categories[runner.AgeCategory] += 1
        
        print("\n" + "-"*40)
        print(f"{'Category':<15} {'Count':<10} {'Percentage':<10}")
        print("-"*40)
        
        total = len(self.runners)
        for category, count in categories.items():
            percentage = (count / total) * 100 if total > 0 else 0
            print(f"{category:<15} {count:<10} {percentage:.1f}%")
        
        print("-"*40)
        print(f"\n   Total Runners: {total}")
    
    def discount_report(self):
        """Discount Report - Textbook Chapter 8: Cross Tabulation"""
        print("\n" + "="*58)
        print("                  DISCOUNT REPORT")
        print("="*58)
        print(f"   Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*58)
        
        discount_applied = {
            "Senior (20%)": 0,
            "Under 18 (15%)": 0,
            "Club Member (10%)": 0,
            "Early Bird (10%)": 0,
            "No Discount": 0
        }
        
        for runner in self.runners:
            if runner.HighestDiscount == DISCOUNT_SENIOR:
                discount_applied["Senior (20%)"] += 1
            elif runner.HighestDiscount == DISCOUNT_UNDER18:
                discount_applied["Under 18 (15%)"] += 1
            elif runner.HighestDiscount == DISCOUNT_CLUBMEMBER:
                discount_applied["Club Member (10%)"] += 1
            elif runner.HighestDiscount == DISCOUNT_EARLYBIRD:
                discount_applied["Early Bird (10%)"] += 1
            else:
                discount_applied["No Discount"] += 1
        
        print("\n" + "-"*50)
        print(f"{'Discount Type':<20} {'Count':<10} {'Percentage':<10}")
        print("-"*50)
        
        total = len(self.runners)
        for discount_type, count in discount_applied.items():
            if count > 0:
                percentage = (count / total) * 100 if total > 0 else 0
                print(f"{discount_type:<20} {count:<10} {percentage:.1f}%")
        
        print("-"*50)
        print(f"\n   Total Runners: {total}")
    
    def income_report(self):
        """Income Report - Textbook Chapter 7: Accumulating"""
        print("\n" + "="*58)
        print("                  INCOME REPORT")
        print("="*58)
        print(f"   Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*58)
        
        # Accumulate totals by race distance - Textbook Chapter 8
        race_income = {5: 0, 10: 0, 21: 0, 42: 0}
        race_counts = {5: 0, 10: 0, 21: 0, 42: 0}
        
        for runner in self.runners:
            race_income[runner.RaceDistance] += runner.FinalFee
            race_counts[runner.RaceDistance] += 1
        
        print("\n" + "-"*50)
        print(f"{'Race Distance':<15} {'Entries':<10} {'Total Income':<15}")
        print("-"*50)
        
        grand_total = 0
        total_entries = 0
        
        for distance in [5, 10, 21, 42]:
            income = race_income[distance]
            count = race_counts[distance]
            grand_total += income
            total_entries += count
            print(f"{distance} km{' ':<8} {count:<10} R{income:.2f}")
        
        print("-"*50)
        print(f"{'TOTAL':<15} {total_entries:<10} R{grand_total:.2f}")
        print("-"*50)


# ============================================================
# MAIN PROGRAM - Textbook Chapter 3: Coding the Solution
# ============================================================

def main():
    """Main program entry point"""
    system = RegistrationSystem()
    system.run()

if __name__ == "__main__":
    main()


# Follow me on GitHub https://github.com/KKM196