VALID_DOMAINS=[".bg",".org",".net",".com"]
class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

email=input()
def get_tld(domain):
    return f".{domain.split('.')[-1]}"

# todo това не съм го осмислила
def has_valid_top_level_domain(domain):
    return any([tld==get_tld(domain) for tld in VALID_DOMAINS])


while email!="End":
    if "@" not in email:
        raise MustContainAtSymbolError("Must contain symbol @")

    name,domain=email.split("@")
    if len(name)<=4:
        raise NameTooShortError("Name must be more than 4 characters")
    if not has_valid_top_level_domain(domain):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")







    print("Email is valid")
    email=input()