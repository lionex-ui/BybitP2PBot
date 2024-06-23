from typing import TypedDict, List


class Orders:

    class RequestJson(TypedDict, total=False):
        userId: int
        tokenId: str
        currencyId: str
        payment: List[str]
        amount: str
        authMaker: bool
        canTrade: bool
        side: str
        size: str
        page: str

    class RequestResponse(TypedDict):
        ret_code: int
        ret_msg: str
        result: "Orders.ResultResponse"

    class ResultResponse(TypedDict):
        count: int
        items: List["Orders.ItemResponse"]

    class ItemResponse(TypedDict):
        id: str
        accountId: str
        userId: str
        nickname: str
        tokenId: str
        tokenName: str
        currencyId: str
        side: int
        priceType: int
        price: str
        premium: str
        lastQuantity: str
        quantity: str
        frozenQuantity: str
        executedQuantity: str
        minAmount: str
        maxAmount: str
        remark: str
        status: int
        createDate: str
        payments: List[str]
        orderNum: int
        finishNum: int
        recentOrderNum: int
        recentExecuteRate: int
        fee: str
        isOnline: bool
        lastLogoutTime: str
        blocked: str
        makerContract: bool
        symbolInfo: "Orders.SymbolInfoResponse"
        tradingPreferenceSet: "Orders.TradingPreferenceSetResponse"
        version: int
        authStatus: int
        recommend: bool
        recommendTag: str

    class SymbolInfoResponse(TypedDict):
        id: str
        exchangeId: str
        orgId: str
        currencyId: str
        status: int
        lowerLimitAlarm: int
        upperLimitAlarm: int
        itemDownRange: str
        itemUpRange: str
        currencyMinQuote: str
        currencyMaxQuote: str
        currencyLowerMaxQuote: str
        tokenMinQuote: str
        tokenMaxQuote: str
        kycCurrencyLimit: str
        itemSideLimit: int
        buyFeeRate: str
        sellFeeRate: str
        orderAutoCancelMinute: int
        orderFinishMinute: int
        tradeSide: int
        currency: "Orders.CurrencyResponse"
        token: "Orders.TokenResponse"

    class CurrencyResponse(TypedDict):
        id: str
        exchangeId: str
        orgId: str
        currencyId: str
        scale: int

    class TokenResponse(TypedDict):
        id: str
        exchangeId: str
        orgId: str
        currencyId: str
        scale: int
        sequence: int

    class TradingPreferenceSetResponse(TypedDict):
        hasUnPostAd: int
        isKyc: int
        isEmail: int
        isMobile: int
        hasRegisterTime: int
        registerTimeThreshold: int
        orderFinishNumberDay30: int
        completeRateDay30: str
        nationalLimit: str
        hasOrderFinishNumberDay30: int
        hasCompleteRateDay30: int
        hasNationalLimit: int
