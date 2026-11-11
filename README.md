<a href="https://www.ladicodes.dev">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img alt="ladicodes: build, write, teach, ship" src="assets/banner-light.svg" width="100%">
  </picture>
</a>

<h1 align="center">Hey, I'm Ladipo Samuel 👋</h1>

<p align="center">
  Most people know me as <b>Ladicodes</b>.<br>
  <b>Developer Relations Engineer · Blockchain Builder · Backend Engineer</b>
</p>

<p align="center">
  I build backend systems and developer tools, then write about how they work so the next developer has an easier time than I did.
</p>

<p align="center">
  <a href="https://www.ladicodes.dev"><img alt="Portfolio: ladicodes.dev" src="https://img.shields.io/badge/ladicodes.dev-visit_my_portfolio-22D3EE?style=for-the-badge&labelColor=1E293B"></a>
  <br>
  <a href="https://x.com/ladicodez"><img alt="X: @ladicodez" src="https://img.shields.io/badge/X-@ladicodez-1E293B?style=flat-square&logo=x&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ladicodes"><img alt="LinkedIn: ladicodes" src="https://img.shields.io/badge/LinkedIn-ladicodes-1E293B?style=flat-square&logoColor=white"></a>
  <a href="https://dev.to/ladipo_samuel_7cfaa827bf5"><img alt="DEV.to articles" src="https://img.shields.io/badge/DEV-articles-1E293B?style=flat-square&logo=devdotto&logoColor=white"></a>
</p>

---

## A little about me

I'm a Computer Science student at the University of Lagos. I interned at **Microsoft**, where I was picked as lead intern and left with the Excellence and Collaboration Award, then spent a year as a software engineer at **Squad by GTCO**, building backend services in fintech. Fintech is where I learned to care about the boring details that keep money safe.

These days I'm deep in **Solana**. I graduated from the Turbin3 builders cohort and I'm writing my way through SPL tokens one article at a time. I also like poking at AI systems to see how they break.

Outside the editor I'm usually around a community: GDG UNILAG, Solana Student Academy, judging a hackathon, or answering DMs from someone who just started. I've won 12 hackathons, and honestly most of that credit goes to good teams and a clear pitch.

## What I do

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🛠️ Build</h3>
      Backend services and APIs in Python and TypeScript, plus tools that make other developers faster. Payments, webhooks, auth and the plumbing nobody sees.
    </td>
    <td width="50%" valign="top">
      <h3>⛓️ Blockchain</h3>
      Solana programs with Anchor, SPL tokens and stablecoin payment flows. I've also shipped on Sui and NEAR at hackathons.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>✍️ Teach</h3>
      Tutorials that explain the architecture before the first command. Talks, panels, workshops and mentoring student teams.
    </td>
    <td width="50%" valign="top">
      <h3>🤝 Community</h3>
      Growing developer communities on campus and online, and helping new developers land their first opportunity.
    </td>
  </tr>
</table>

## Featured projects

### [LogJack](https://github.com/ladicodes/LogJack)
<sub><i>solo project</i></sub><br>
A testbed for indirect prompt injection. It hides attack strings inside synthetic security logs (User-Agent headers, URL paths, SSH usernames) and measures whether an LLM-powered SOC assistant gets talked out of the right verdict, comparing four defense strategies on identical inputs. Runs fully simulated, with a mock provider for development and adapters for real models.<br>
<sub>Python · FastAPI · React · TypeScript</sub> · [Repo](https://github.com/ladicodes/LogJack) · [Live demo](https://log-jack.vercel.app)

### [BlockRouter](https://github.com/haileyesus2433/BlockRouter)
<sub><i>Turbin3 capstone, team project led by [haileyesus2433](https://github.com/haileyesus2433)</i></sub><br>
Self-custodial stablecoin payments for AI inference on Solana. Lock a capped USDC budget in a vault PDA, point any OpenAI-compatible tool at the relayer, and pay for exact token usage on-chain. Whatever a session doesn't spend goes back to your vault. Deployed on devnet. I contributed to the build and made the pitch deck.<br>
<sub>Rust · Anchor · TypeScript · Solana</sub> · [Repo](https://github.com/haileyesus2433/BlockRouter) · [Web app](https://blockrouter.netlify.app) · [Pitch deck](https://blockrouter-presentation.vercel.app)

### [StakeSync](https://www.usestakesync.xyz/)
<sub><i>team project</i></sub><br>
Put money behind your goals, prove you followed through, and earn rewards. You stake USDC on a challenge, progress is checked against sources like GitHub, LeetCode or your Solana wallet, and people who quit fund the people who don't. Supports USDC on Solana and Stellar.<br>
<sub>TypeScript · React · Solana · Stellar</sub> · [Live app](https://www.usestakesync.xyz/) · [Pitch deck](https://stakesync-demo.vercel.app)

### [Fliq](https://github.com/FliqLabs/Fliq)
<sub><i>team project, in progress at the NEAR Hackathon (Nov 2026)</i></sub><br>
A payout API that turns stablecoins into local bank and mobile money, routed to the best after-fee rate across off-ramp providers. A NEAR contract enforces spending caps so AI agents can pay without overspending. I work on the API: key management, signed webhooks with retries, payout history, and the deposit watcher.<br>
<sub>TypeScript · NEAR · Rust · Docker</sub> · [Repo](https://github.com/FliqLabs/Fliq) · [Site](https://fliq-delta.vercel.app)

### [Sovra](https://github.com/Kingvic300/Sovra)
<sub><i>hackathon team project with [Kingvic300](https://github.com/Kingvic300)</i></sub><br>
A personal finance app that remembers your goals, limits and decisions in a memory vault on Walrus. Built for the Tatum x Walrus "Total Recall" hackathon. I built Sui USDC transaction sync, budget suggestions, reminders, and data export and deletion.<br>
<sub>TypeScript · Sui · Walrus</sub> · [Repo](https://github.com/Kingvic300/Sovra) · [Live app](https://sovra-ecru.vercel.app)

## Writing and developer education

I write the tutorials I wish I'd had: architecture first, then code. A few favourites:

**Solana, from the ground up**
- [Building on Solana with Turbin3: Understanding the Architecture First](https://dev.to/ladipo_samuel_7cfaa827bf5/building-on-solana-with-turbin3-understanding-the-architecture-first-2fm8)
- Building an SPL Token, a three-part series: [Creating the Mint](https://dev.to/ladipo_samuel_7cfaa827bf5/building-an-spl-token-creating-the-mint-gi7) → [Adding Metadata](https://dev.to/ladipo_samuel_7cfaa827bf5/building-an-spl-token-on-solana-adding-metadata-e5f) → [Minting Tokens and Understanding ATAs](https://dev.to/ladipo_samuel_7cfaa827bf5/building-an-spl-token-on-solana-minting-tokens-and-understanding-atas-3hpl)

**Backend engineering**
- [Beyond CRUD: 9 Backend Concepts Every Engineer Should Know to Build Scalable and Reliable Systems](https://dev.to/ladipo_samuel_7cfaa827bf5/beyond-crud-9-backend-concepts-every-engineer-should-know-to-build-scalable-and-reliable-systems-4af3)
- Docker Explained, a beginner series: [Part 1](https://dev.to/ladipo_samuel_7cfaa827bf5/docker-explained-part-1-understanding-docker-before-writing-your-first-command-3o0o) · [Part 2](https://dev.to/ladipo_samuel_7cfaa827bf5/docker-explained-part-2-understanding-dockers-architecture-images-containers-1fop) · [Part 3](https://dev.to/ladipo_samuel_7cfaa827bf5/docker-series-part-3dockerizing-your-first-application-1ji6)

**Growing as a developer**
- [The Strategy Behind Winning Hackathons](https://dev.to/ladipo_samuel_7cfaa827bf5/the-strategy-behind-winning-hackathons-3b33)

More on [DEV](https://dev.to/ladipo_samuel_7cfaa827bf5). Off the page, I've spoken at TechPulse on developer advocacy, mentored and spoken at the Hult Prize, been a panelist at tech events, and designed and judged hackathon challenges.

## Experience and communities

- **Microsoft Nigeria** · Software Engineering Intern. Lead intern, Excellence and Collaboration Award.
- **Squad by GTCO** · Software Engineer. Backend services in fintech, and the [Hackademy](https://github.com/ladicodes/Squad-Hackademy) developer education portal.
- **Turbin3** · Solana builders cohort, graduate. Anchor programs for an [escrow](https://github.com/ladicodes/assignment_2_escrow), an [AMM](https://github.com/ladicodes/assignment_3_amm), [Token-2022](https://github.com/ladicodes/assignment_4_token22) and [NFT staking](https://github.com/ladicodes/assignment_5_nft_staking).
- **GDG UNILAG** · Team Lead, Publicity & Community.
- **Solana Student Academy** · Community Manager, onboarding students to Solana through workshops and hands-on projects.
- Also: Millennium Fellow, and represented Nigeria at the FIRST Global Challenge.

## Tech stack

<table>
  <tr><td><b>Languages</b></td><td><img alt="Python" src="https://img.shields.io/badge/Python-1E293B?style=flat-square&logo=python&logoColor=22D3EE"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-1E293B?style=flat-square&logo=typescript&logoColor=22D3EE"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-1E293B?style=flat-square&logo=javascript&logoColor=22D3EE"> <img alt="Rust" src="https://img.shields.io/badge/Rust-1E293B?style=flat-square&logo=rust&logoColor=22D3EE"> <img alt="Java" src="https://img.shields.io/badge/Java-1E293B?style=flat-square&logo=openjdk&logoColor=22D3EE"></td></tr>
  <tr><td><b>Backend</b></td><td><img alt="Django" src="https://img.shields.io/badge/Django-1E293B?style=flat-square&logo=django&logoColor=22D3EE"> <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-1E293B?style=flat-square&logo=fastapi&logoColor=22D3EE"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-1E293B?style=flat-square&logo=nodedotjs&logoColor=22D3EE"> <img alt="Express" src="https://img.shields.io/badge/Express-1E293B?style=flat-square&logo=express&logoColor=22D3EE"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-1E293B?style=flat-square&logo=nestjs&logoColor=22D3EE"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-1E293B?style=flat-square&logo=postgresql&logoColor=22D3EE"></td></tr>
  <tr><td><b>Blockchain</b></td><td><img alt="Solana" src="https://img.shields.io/badge/Solana-1E293B?style=flat-square&logo=solana&logoColor=A78BFA"> <img alt="Anchor" src="https://img.shields.io/badge/Anchor-1E293B?style=flat-square&logoColor=A78BFA"> <img alt="SPL Tokens" src="https://img.shields.io/badge/SPL_%26_Token--2022-1E293B?style=flat-square&logoColor=A78BFA"> <img alt="Sui" src="https://img.shields.io/badge/Sui_·_Move-1E293B?style=flat-square&logo=sui&logoColor=A78BFA"></td></tr>
  <tr><td><b>Frontend</b></td><td><img alt="React" src="https://img.shields.io/badge/React-1E293B?style=flat-square&logo=react&logoColor=22D3EE"> <img alt="Next.js" src="https://img.shields.io/badge/Next.js-1E293B?style=flat-square&logo=nextdotjs&logoColor=22D3EE"> <img alt="Tailwind CSS" src="https://img.shields.io/badge/Tailwind_CSS-1E293B?style=flat-square&logo=tailwindcss&logoColor=22D3EE"></td></tr>
  <tr><td><b>Tools</b></td><td><img alt="Docker" src="https://img.shields.io/badge/Docker-1E293B?style=flat-square&logo=docker&logoColor=22D3EE"> <img alt="Azure" src="https://img.shields.io/badge/Azure-1E293B?style=flat-square&logoColor=22D3EE"> <img alt="Vercel" src="https://img.shields.io/badge/Vercel-1E293B?style=flat-square&logo=vercel&logoColor=22D3EE"> <img alt="Git" src="https://img.shields.io/badge/Git-1E293B?style=flat-square&logo=git&logoColor=22D3EE"></td></tr>
</table>

## Open source

My most-used open-source repo is **[DSA Solutions and Patterns](https://github.com/ladicodes/DSA-Solutions-and-Patterns)**. I solve a problem, name the pattern behind it, and explain the thinking so you can reuse the idea and not just the answer. Other developers contribute their solutions too.

<a href="https://github.com/ladicodes/DSA-Solutions-and-Patterns"><img alt="Stars" src="https://img.shields.io/github/stars/ladicodes/DSA-Solutions-and-Patterns?style=flat-square&labelColor=1E293B&color=2DD4BF&logo=github"></a> <a href="https://github.com/ladicodes/DSA-Solutions-and-Patterns/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/ladicodes/DSA-Solutions-and-Patterns?style=flat-square&labelColor=1E293B&color=2DD4BF"></a>

My day-to-day activity is in the contribution graph just below.

## Let's build something

If you're building developer tools, working on something in the Solana ecosystem, writing docs that need a friendly second pair of eyes, or putting together an event and need a speaker, I'd love to hear about it. I also enjoy contributing to open source and working with developer communities. My X DMs are open, and that's usually the fastest way to reach me.

<p align="center">
  <a href="https://www.ladicodes.dev"><b>Portfolio</b></a> ·
  <a href="https://x.com/ladicodez"><b>X</b></a> ·
  <a href="https://www.linkedin.com/in/ladicodes"><b>LinkedIn</b></a> ·
  <a href="https://dev.to/ladipo_samuel_7cfaa827bf5"><b>DEV</b></a>
</p>

<p align="center"><i>Happy building 💜</i></p>
