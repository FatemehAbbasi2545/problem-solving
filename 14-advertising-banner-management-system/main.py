from typing import NamedTuple, List, Dict, Iterator, Optional
import random

class Banner(NamedTuple):
    name: str
    width: int
    height: int
    ctr: float # Hypothetical: Click-through rate for display

class Campaign(NamedTuple):
    name: str
    banners: List[Banner]
    weights: Optional[List[float]] = None # If not, we use CTR for weight.
    seed: Optional[int] = None # For repeatable random generation

class BannerBase:
    def render(self) -> str:
        raise NotImplementedError

class WeightedBanner(BannerBase):
    def __init__(self, banner: Banner):
        self.banner = banner

    def render(self) -> str:
        return f"Banner({self.banner.name}, {self.banner.width}x{self.banner.height})"

class CampaignManager:
    def __init__(self, campaign: Campaign):
        self.campaign = campaign
        self._rng = random.Random(campaign.seed)
        self._cache: Dict[str, int] = {}

        if campaign.weights and len(campaign.weights) == len(campaign.banners):
            self.weights = campaign.weights
        else:
            self.weights = [b.ctr for b in campaign.banners]

        if len(self.weights) != len(campaign.banners):
            raise ValueError("Weights should be equal to the number of banners.")

    def _choose_index(self) -> int:
        # Select a banner with linear/relative weight
        total = sum(self.weights)
        if total <= 0:
            return self._rng.randrange(len(self.campaign.banners))
        pick = self._rng.uniform(0, total)
        acc = 0.0
        for i, w in enumerate(self.weights):
            acc += w
            if pick <= acc:
                return i
        return len(self.campaign.banners) - 1

    def banner_stream(self) -> Iterator[Banner]:
        """Generator: Produces a banner each time according to the weights."""
        index = 0
        while True:
            idx = self._choose_index()
            banner = self.campaign.banners[idx]
            key = f"{self.campaign.name}:{banner.name}"
            self._cache[key] = self._cache.get(key, 0) + 1
            yield banner
            index += 1

    def report(self) -> str:
        lines = ["Banner broadcast report:"]
        for b in self.campaign.banners:
            key = f"{self.campaign.name}:{b.name}"
            count = self._cache.get(key, 0)
            lines.append(f"- Banner {b.name}: shows = {count}")
        return "\n".join(lines)

if __name__ == "__main__":
    banners = [
        Banner("Top-Banner", 728, 90, 0.5),
        Banner("Sidebar", 300, 250, 0.2),
        Banner("Footer", 970, 90, 0.3),
    ]
    camp = Campaign("SpringLaunch", banners, seed=42)
    manager = CampaignManager(camp)

    stream = manager.banner_stream()
    for _ in range(10):
        b = next(stream)
        print("Displayed:", b)

    print(manager.report())
