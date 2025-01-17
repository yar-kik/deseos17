from abc import abstractmethod
from typing import Protocol, List

from deseos17.domain.models.sharing import ShareRule
from deseos17.domain.models.user_id import UserId
from deseos17.domain.models.wish import WishListId, WishId, Wish, WishList


class Comitter(Protocol):
    @abstractmethod
    def commit(self):
        raise NotImplementedError


class WishReader(Protocol):
    @abstractmethod
    def get_wish(self, wish_id: WishId) -> Wish:
        raise NotImplementedError


class WishSaver(Protocol):
    @abstractmethod
    def save_wish(self, wish: Wish) -> None:
        raise NotImplementedError


class WishListReader(Protocol):
    @abstractmethod
    def get_wishlist(self, wishlist_id: WishListId) -> WishList:
        raise NotImplementedError


class WishListSaver(Protocol):
    @abstractmethod
    def save_wishlist(self, wish: WishList) -> None:
        raise NotImplementedError


class ShareReader(Protocol):
    @abstractmethod
    def get_share_rules(
            self, wishlist_id: WishListId, user_id: UserId,
    ) -> List[ShareRule]:
        raise NotImplementedError
