object Squares_Reactive extends SimpleSwingApplication {


    // −− APPLICATION LOGIC −−−−−−−−−−−−−−−−−−−−
    object square1 {
        val position = Signal {
            Point(time().s ∗ 100, 100)
        }
    }
    object square2 {
        val v = Signal {
            time().s ∗ 100
        }
        val position = Signal {
            Point(time().s ∗ v(), 200)
        }
    }


    // painting components
    (square1.position.changed || square2.position.changed) += {
        _ => Swing onEDT { top.repaint }
    }

    // −− Graphics −−−−−−−−−−−−−−−−−−−−−
    lazy val panel: RePanel = new RePanel {
        override def paintComponent(g: Graphics2D) {
            super.paintComponent(g)
        g.fillRect(
            square1.position.getValue.x.toInt − 8,
            square2.position.getValue.y.toInt − 8,
            16, 16)
        g.fillRect(
            square1.position.getValue.x.toInt − 8,
            square2.position.getValue.y.toInt − 8,
            16, 16)
        }
    }

    lazy val top = new MainFrame {
        preferredSize = new Dimension(800, 400)
        contents = panel
    }
}
