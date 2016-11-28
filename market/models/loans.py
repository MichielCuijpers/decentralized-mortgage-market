class LoanRequest(object):
    def __init__(self, id, user_key, house_id, mortgage_type, banks, personal_info, amount_wanted):
        assert isinstance(id, str)
        assert isinstance(user_key, str)
        assert isinstance(house_id, str)
        assert isinstance(mortgage_type, int)
        assert isinstance(banks, list)
        assert isinstance(personal_info, unicode)
        assert isinstance(amount_wanted, int)

        self._id = id
        self._user_key = user_key
        self._house_id = house_id
        self._mortgage_type = mortgage_type
        self._banks = banks
        self._personal_info = personal_info
        self._amount_wanted = amount_wanted


class Loan(object):
    def __init__(self, id, request_id, user_key, house_id, bank, amount, mortgage_type, interest_rate, max_invest_rate, default_rate, duration, risk, investors):
        assert isinstance(id, str)
        assert isinstance(request_id, str)
        assert isinstance(user_key, str)
        assert isinstance(house_id, str)
        assert isinstance(bank, str)
        assert isinstance(amount, int)
        assert isinstance(mortgage_type, int)
        assert isinstance(interest_rate, float)
        assert isinstance(max_invest_rate, float)
        assert isinstance(default_rate, float)
        assert isinstance(duration, int)
        assert isinstance(risk, str)
        assert isinstance(investors, list)

        self._id = id
        self._request_id = request_id
        self._user_key = user_key
        self._house_id = house_id
        self._bank = bank
        self._amount = amount
        self._mortgage_type = mortgage_type
        self._interest_rate = interest_rate
        self._max_invest_rate = max_invest_rate
        self._default_rate = default_rate
        self._duration = duration
        self._risk = risk
        self._investors = investors


class Investment(object):
    def __init__(self, id, user_key, amount, duration, interest_rate, loan_id, accepted):
        assert isinstance(id, str)
        assert isinstance(user_key, str)
        assert isinstance(amount, int)
        assert isinstance(duration, int)
        assert isinstance(interest_rate, float)
        assert isinstance(loan_id, str)
        assert isinstance(accepted, bool)

        self._id = id
        self._user_key = user_key
        self._amount = amount
        self._duration = duration
        self._interest_rate = interest_rate
        self._loan_id = loan_id
        self._accepted = accepted