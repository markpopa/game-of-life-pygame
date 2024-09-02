**3. Maak een Branch Aan**
Om een branch te maken in Git:
**Maak een Branch Aan**:

```
bash
```

Copy code
`git branch nieuwe-branch-naam`
Vervang `nieuwe-branch-naam` door de naam die je voor de branch wilt gebruiken.
**Schakel over naar de Nieuwe Branch**:

```
bash
```

Copy code
`git checkout nieuwe-branch-naam`
Als alternatief kun je een branch maken en er direct naartoe schakelen met één commando:

```
bash
```

Copy code
`git checkout -b nieuwe-branch-naam`
**4. Werk aan Je Branch**
**Maak Wijzigingen**: Bewerk bestanden, voeg nieuwe bestanden toe of verwijder bestanden indien nodig voor je functie of oplossing.
**Voeg Wijzigingen Toe**:

```
bash
```

Copy code
`git add .`
Dit voegt alle wijzigingen toe. Je kunt ook specifieke bestanden toevoegen:

```
bash
```

Copy code
`git add bestand1 bestand2`
**Commit Wijzigingen**:

```
bash
```

Copy code
`git commit -m "Je commit-bericht"`
Schrijf een betekenisvol commit-bericht waarin je je wijzigingen beschrijft.
**5. Push Je Branch naar een Remote Repository**
Als je werkt met een remote repository en je wilt je branch delen:
**Push de Branch**:

```
bash
```

Copy code
`git push origin nieuwe-branch-naam`
Dit uploadt je branch en de commits naar de remote repository.
**Maak een Pull Request** (optioneel, op platforms zoals GitHub, GitLab, Bitbucket):
* Ga naar je repository op het platform.
* Je ziet meestal een optie om een pull request (PR) te maken voor de branch die je zojuist hebt gepusht.
* Volg de instructies van het platform om de PR te maken en in te dienen voor review en samenvoegen.
**6. Schakel Tussen Branches**
Om terug te schakelen naar een andere branch:

```
bash
```

Copy code
`git checkout branch-naam`
**7. Merge Branches**
Als je functie of oplossing klaar is en je wilt deze samenvoegen met de hoofdbranch (vaak `main` of `master`):
**Schakel over naar de Hoofdbranch**:

```
bash
```

Copy code
`git checkout main`
**Merge de Feature Branch**:

```
bash
```

Copy code
`git merge nieuwe-branch-naam`
**Push de Bijgewerkte Hoofdbranch**:

```
bash
```

Copy code
`git push origin main`
**8. Verwijder een Branch**
Na het samenvoegen wil je misschien de branch verwijderen:
**Verwijder een Lokale Branch**:

```
bash
```

Copy code
`git branch -d nieuwe-branch-naam`
Gebruik `-D` om geforceerd te verwijderen als de branch niet samengevoegd is:

```
bash
```

Copy code
`git branch -D nieuwe-branch-naam`
**Verwijder een Remote Branch**:

```
bash
```

Copy code
`git push origin --delete nieuwe-branch-naam`
**Samenvatting**
* **Maak Aan**: `git branch branch-naam`
* **Schakel Over**: `git checkout branch-naam`
* **Maak en Schakel Over**: `git checkout -b branch-naam`
* **Push**: `git push origin branch-naam`
* **Merge**: `git merge branch-naam`
* **Verwijder**: `git branch -d branch-naam` (lokaal), `git push origin --delete branch-naam` (remote)

## Contributing
As a team we need to know what were working in on so here is a link a to scrumboard and on that board are things that as a team,
we each need to do each person has on objective here's a link to the scrumboard:  https://lucid.app/lucidspark/455622f1-bad0-4165-a809-35737e9d2449/edit?viewport_loc=-13187%2C4048%2C4554%2C2161%2C0_0&invitationId=inv_5bca598b-7734-4674-9798-bd6154b178b7
