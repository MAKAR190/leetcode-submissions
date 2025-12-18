# Problem definition

# Filter each email in emails, using '+' and '.' rules both in local name and domain name, and count how many different emails will recieve mails based on outcomes of those rules after applying for each email

# Edge cases

# No edge cases for now

# Approach

# Implement the additional function which will apply to each email in emails by using those rules ('.' and '+'), by splitting the email in local and domain parts, then it will convert it to an actual forward email and return

# Iterate through all emails and apply that function to each email and in each iteration I will add that converted email to a set of unique emails, and then after all iterations I will return the set length which is the actual number of different emails from emails list

# TC and SC

# TC(O(n = 100 + m = 100)) SC(O(n = 100));  n - len(emails), m - average length of a string = 100



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        unique_emails = set()
        
        def filter_email(email: str) -> str:
            local, domain = email.split("@")
            
            local_filtered = []
            
            for c in local:
                if c == "+":
                    break
                    
                if c != ".":
                    local_filtered.append(c)
                    
            local_filtered = "".join(local_filtered)
            return local_filtered + "@" + domain
        
        for email in emails:
            unique_emails.add(filter_email(email))
        
        return len(unique_emails)
            
            
